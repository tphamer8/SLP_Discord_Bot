<h1>Role Verifcation Discord Bot</h1>
<!-- ### [YouTube Demonstration](https://youtu.be/7eJexJVCqJo) -->
<h2 style="color: darkblue;">Description</h2>
This Discord bot is designed to automatically verify a user's purchase of a STEM Launch Program course and assign them the appropriate role to access their session-specific text and voice channels. It functions by cross-referencing the user’s provided Order Number and email address against a Google Sheet populated by Make, a software automation tool. Make integrates the orders from the STEM Launch Program’s Squarespace website into the sheet, keeping it up-to-date with purchases.
<br />

<h2 style="color: darkblue;">Languages and Utilities Used</h2>

- <b>AWS</b>
- <b>Python</b>
- <b>Google Sheets</b>
- <b>Make</b>


<h2>Program walk-through:</h2>
1. When a user joins the Discord server, they are prompted to verify their account by first typing "!verify" in the #verification channel
<img src="https://imgur.com/Pt9Pe21.png" height="100%" width="100%" alt="Welcome/Verifcation Message"/>
2. 

The bot retrieves the corresponding data from the Google Sheet, verifying the order number and email address.
<img src="https://github.com/tphamer8/SLP_Discord_Bot/blob/main/SLP%20Bot%20Message%20Photo.jpg" height="100%" width="100%" alt="Welcome/Verifcation Message"/>

If a match is found, the bot assigns the appropriate role to the user, granting access to the correct session channels.

If there is no match, the bot informs the user of the issue (e.g., invalid credentials) and prevents them from accessing the channels.


<p align="center">
Add the new hire entry to the sheet and click the checkbox: <br/>
<img src="https://imgur.com/W0vQPRw.png" height="100%" width="100%" alt="Disk Sanitization Steps"/>
<br />
<br />
The email will automatically send from the address of the spreadsheet editor: <br/>
<img src="https://imgur.com/QoF99dn.png" height="100%" width="100%" alt="Disk Sanitization Steps"/>
<br />

<a href="https://github.com/tphamer8/SLSAutomatedEmailSystem/blob/main/autoEmailScript.js">Link to code</a>


<!--
<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/62TgaWL.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Select the disk:  <br/>
<img src="https://i.imgur.com/tcTyMUE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the number of passes: <br/>
<img src="https://i.imgur.com/nCIbXbg.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Confirm your selection:  <br/>
<img src="https://i.imgur.com/cdFHBiU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Wait for process to complete (may take some time):  <br/>
<img src="https://i.imgur.com/JL945Ga.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sanitization complete:  <br/>
<img src="https://i.imgur.com/K71yaM2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Observe the wiped disk:  <br/>
<img src="https://i.imgur.com/AeZkvFQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>
-->

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
-->
