# Subtitles

**Category:** Forensics
**Difficulty:** Hard
**Author:** iCiaran

## Description

The intern was supposed to create subtitles for this video, but they've made quite a few "mistakes", maybe they're not mistakes after all?
Flag is in the format `ictf{[a-z_]*}`

## Distribution

- subtitles.mp4
- subtitles.srt

## Deploy notes

N/A

## Solution

- Sample solve script in repo
  - Parse the subtitles file to get the number from each frame
  - Take each frame from the video and extract the number from it
  - Compare, where different take note of the subtitle values
- `ictf{i_hope_you_didnt_do_this_by_hand}`
