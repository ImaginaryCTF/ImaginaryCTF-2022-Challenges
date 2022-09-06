# ogre

**Category:** Forensics
**Difficulty:** Easy
**Author:** iCiaran

## Description

What are you doing in my swamp?!

## Distribution

- docker pull ghcr.io/iciaran/ogre:ctf

## Deploy notes

Make image public before ctf

## Solution

- Save the docker image `docker image save ogre > /tmp/ogre.tar`
- Untar
- Compare the layers
- See `/tmp/secret` was created and then deleted
- `ictf{onions_have_layers_images_have_layers}`
