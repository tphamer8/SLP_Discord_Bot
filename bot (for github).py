import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Google Sheets Setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDENTIALS_FILE = "credentials.json"
SPREADSHEET_NAME = "Program Registration" # Spreadsheet name

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPE)
gc = gspread.authorize(credentials)
sheet = gc.open(SPREADSHEET_NAME).sheet1

# Tracks used order numbers
used_order_numbers = set()

# Command to start verification
@bot.command()
async def verify(ctx):
    if ctx.channel.name != "verification":
        await ctx.send("❌ This command can only be used in the #verification channel.")
        return

    # Delete the user's "!verify" message
    await ctx.message.delete()

    # Send a DM to the user
    try:
        await ctx.author.send("Please enter your Order Number and Customer Email separated by a space.")
    except discord.Forbidden:
        await ctx.send("❌ I couldn't send you a DM. Please make sure your DMs are open.")

# DMs for verification
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    
    if isinstance(message.channel, discord.DMChannel):
        inputs = message.content.strip().split(" ")
        if len(inputs) != 2:
            await message.channel.send("❌ Please provide both your Order Number and Customer Email, separated by a space.")
            return

        order_number = inputs[0]
        customer_email = inputs[1].lower()  # Convert to lowercase

        # Check if the order number has been used
        if order_number in used_order_numbers:
            await message.channel.send("❌ This Order Number has already been used for verification.")
            return

        try:
            records = sheet.get_all_records()
            for row in records:
                order_from_sheet = str(row["Order #"]).strip()
                email_from_sheet = row["Customer Email"].strip().lower()

                # Check if both order number and email match
                if order_from_sheet == order_number and email_from_sheet == customer_email:
                    product_name = row["Product Name"]  # Get product name from the record

                    # Find the role to assign based on the product
                    guild = bot.get_guild()  # Server ID hidden
                    member = guild.get_member(message.author.id)

                    # Assign roles based on product name
                    if product_name == "Spring Computer Programming Session":
                        role_name = "spring-2025-cs"
                    else:
                        await message.channel.send("❌ Unknown session. Please contact support.")
                        return

                    # Find the role in the server and assign it
                    role = discord.utils.get(guild.roles, name=role_name)
                    if role and member:
                        await member.add_roles(role)
                        await message.channel.send(f"✅ Verification successful! You have been assigned the '{role_name}' role.")
                        used_order_numbers.add(order_number)  # Mark the Order Number as used
                        return
                    else:
                        await message.channel.send("❌ Unable to assign the role. Please contact an admin.")
                        return

            # If Order Number or Customer Email is not found
            await message.channel.send("❌ Order Number or Customer Email not found in the records. Please check your input.")
        except Exception as e:
            await message.channel.send(f"❌ An error occurred: {str(e)}")

    await bot.process_commands(message)

# Run the bot
bot.run("")  # Bot token hidden