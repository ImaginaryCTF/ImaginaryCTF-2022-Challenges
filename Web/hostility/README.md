# Hostility
**Category:** Web
**Difficulty:** Medium
**Author:** puzzler7

## Description

I made a file hosting site! Just don't expect to get your files back...

## Distribution

- Website link

## Deploy notes

- Requires `restart: always` in the docker-compose file.
- Needs to run as root so the player can modify `/etc/hosts`.

## Solution

Uploading a file with the name `../../etc/hosts` and the the text `[your_server_ip]\tlocalhost` will overwrite the `/etc/hosts` file, causing it to think that localhost points to your IP. Hosting a server at this IP will see the flag.

Note that this is not an instanced challenge, so players will be fighting with each other to have control over the hosts file.
