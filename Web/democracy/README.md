# Democracy
**Category:** Web
**Difficulty:** Medium
**Author:** puzzler7

## Description

I'm tired of all these skill-based CTF challenges. Y'know what we need more of here? Politics! Simply convince (or strongarm) your fellow competitors to vote for you. The top 1% of players who have the most votes (or top 50, whichever is less) will recieve the flag. This voting will occur 5 times per hour. Keep in mind that no matter how many accounts you make, you can only vote once per IP. Good luck, and happy campaigning!

## Distribution

- Website link

## Deploy notes

- Requires `restart: always` in the docker-compose file.

## Solution

There are two ways that players can try to get the flag. The first is by making a large number of dummy accounts - even though you can only vote once, making more accounts increases the number of people that win.

Second, there is a trivial XSS in the username, and all of the users with non-zero votes are displayed on the main page. A player could write an XSS script to have anyone that visits the main page automatically vote for themself.
