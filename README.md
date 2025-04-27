<h1>Role Verifcation Discord Bot</h1>
<!-- ### [YouTube Demonstration](https://youtu.be/7eJexJVCqJo) -->
<h2 style="color: darkblue;">Description</h2>
This Discord bot is designed to automatically verify a user's purchase of a STEM Launch Program course and assign them the appropriate role to access their course-specific text and voice channels. It functions by cross-referencing the user’s order number, email Address, and purchased course against a Google Sheet populated by Make, a software automation tool. Make integrates the orders from the STEM Launch Program’s Squarespace website into the sheet, keeping it up-to-date with purchases.
<br />

<h2 style="color: darkblue;">Languages and Utilities Used</h2>

- <b>Python</b>
- <b>AWS</b>
- <b>Google Sheets</b>
- <b>Make</b>

<h2>Program walk-through:</h2>
1. When a user joins the Discord server, they are prompted to verify their account by first typing "!verify" in the #verification channel
<img src="https://imgur.com/Pt9Pe21.png" height="100%" width="100%" alt="Welcome/Verifcation Message"/>
<br/>
2. The bot retrieves the corresponding data from the Google Sheet, verifying the order number and email address.
<img src="https://github.com/tphamer8/SLP_Discord_Bot/blob/main/SLP%20Bot%20Message%20Photo.jpg" height="100%" width="100%" alt="Welcome/Verifcation Message"/>
<br/>
3. If a match is found, the bot assigns the appropriate role to the user, granting access to the correct session channels. <br/>
<br/>
4. If there is no match, the bot informs the user of the issue, and the user doesn't obtain access to the channels.
<br/>
<br/>
AWS Instance Hosting: To ensure the bot runs continuously, it is hosted on an AWS EC2 instance. This provides a scalable, reliable, and secure environment, allowing the bot to run 24/7 and handle multiple concurrent verification requests efficiently.
<br/>
<br/>
<a href="https://github.com/tphamer8/SLP_Discord_Bot/blob/main/bot%20(for%20github).py">Link to code</a>
