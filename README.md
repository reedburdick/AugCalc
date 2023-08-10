# AugCalc
Calculates who the top 2 dps are in 30s intervals of a warcraftlogs report

## Setting Up the Program
1. Navigate to the **Releases** section and download the latest executable.
1. Go to this link: [https://www.warcraftlogs.com/api/clients/](https://www.warcraftlogs.com/api/clients/), and create a new client.
2. Name it whatever you want, but ensure it's somewhat descriptive.
3. Set the redirect URL to: `http://localhost:8080/callback`.
4. **Do NOT** check "Public Client".
5. Click create and save both the client ID and client secret in a text file (it's a good idea to delete the file once the program is working).
6. Search "variable" in the Windows search and click "Edit the system environment variables".
7. Click "Environment Variables..." in the bottom right.
8. Create a new system variable:
   - Variable name: `AUG_CLIENT_ID`
   - Variable value: Client ID from the text file.
9. Create another system variable:
   - Variable name: `AUG_CLIENT_SECRET`
   - Variable value: Client Secret from the text file.
10. **Be sure to save the variables somewhere before proceeding.** Restart your PC.
11. Run `AugCalc.exe`.

## Instructions for Use

1. The first question asked is for the code of the report. You can find this in the URL here: `warcraftlogs.com/reports/___#fight=1`.
2. The second question asks how to select which pulls will be used:
   - Fight IDs can be found in the URL of the Warcraft Logs report when a specific pull is selected (look for `fight=`).
   - Encounter IDs will be printed out. Type the number of one or more encounter IDs you wish to be considered, separated by a space.
   - "Phase" means the last phase reached. If you type `3`, ONLY pulls that ENDED in phase 3 will be considered. Multiple phases can be entered, separated by a space.
3. Wait.

## Tips

- If you only select a single fight via any of the selection methods, the program will output links to the relevant segment of the pull so you can verify its data.
- If you select multiple fights, it will tell you how many times of all the pulls you reached each time segment (so you can consider whether to trust the data).
