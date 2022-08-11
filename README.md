# aml-counting-clones

Here is my proposal for automatically collecting number of clones from GitHub Repositories

## Steps to use
1) First all team members need a personal auth token
      a) Create this by entering GitHub and go to profile settings
      b) Scroll down to the bottom and click "Developer Settings" at the bottom of the left nativation panel
      c) Click personal access tokens and generate new token
      d) Make the token never expire and give it access to the entire first repo category
2) Copy this token and send it to the manager or person tracking these clones
3) (ONLY FOR MANAGER/TRACKER) Update the team_database excel file with the team members auth code and alias
4) Now whenever a team member creates a new repository, enter your alias and full github repo into the whitelist_repos (ie cgjhusker/aml-counting-clones)
5) (ONLY FOR MANAGER/TRACKER) When you wish to count clones, run the get_clonesV2 python script with the whitelist as the first argument and database as the second
6) The console will print the total number of clones
