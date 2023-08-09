# AugCalc
Calculates who the top 2 dps are in 30s intervals of a warcraftlogs report

Instructions:
Go to this link: https://www.warcraftlogs.com/api/clients/,  and create a new client
Name it whatever u want, but be descriptive ish
Put "http://localhost:8080/callback" for the redirect URL
Do NOT check "Public Client"
Click create and save both the client ID and client secret in a text file (probably best to delete once the program is working)
Search "variable" in windows search and click "Edit the system environment variables"
Click "Environment Variables..." in the bottom right
Create a new system variable (the bottom box) 
  Variable name: AUG_CLIENT_ID
  Variable value: client ID from text file
Create another system variable
   Variable name: AUG_CLIENT_SECRET
   Variable value: Client Secret from text file
(BE SURE VARIABLES ARE SAVED SOMEWHERE BEFORE DOING THIS STEP) Restart your pc
Run AugCalc.py using your favorite IDE

Instructions for use:
The first question asked is the code for the report. You can find this in the URL here: warcraftlogs.com/reports/___#fight=1
The second question asks how to select which pulls will be used:
 Fight IDs can be found in the URL of the warcraftlogs report when a specific pull is selected (look for fight=)
Encounter IDs will be printed out. Type the number of one or more encounter IDs you wish to be considered, separated by a space
Phase means last phase reached. Meaning, if you type 3, ONLY pulls that ENDED in p3 will be considered. Multiple phases can be entered separated by a space.
Wait

Tips
If you only select a single fight via any of the selection methods, the program will output links to the relevant segment of the pull so you can verify its data
If you select multiple fights, it will tell you how many times of all the pulls you reached each time segment (so you can consider whether to trust the data)