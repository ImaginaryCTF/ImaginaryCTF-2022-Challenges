# Flagbot
**Category:** Misc
**Difficulty:** Easy
**Author:** Astro

## Description

I just learned how to make a cool new Discord bot! I'm storing my secrets on it- I challenge you to try to get the flag! I'm so confident in its security, I'm even going to give you the source. 

## Distribution

- Bot should be invited into the ImaginaryCTF Discord server (don't give the role to anyone other than board)
- flagbot.py provided

## Deploy notes

Run flagbot.py in the same directory as secretstuff.py

## Solution

The bot checks for the role name instead of the role id. If you invite the bot to your own server and make a role called "FlagMaster" and give it to yourself, the $flag command will work.
