#!/bin/bash

rm -rf images
rm -f subtitles.mp4
rm -f subtitles.srt
rm -f output.txt

mkdir -p images

python3 generate.py > output.txt

ffmpeg -framerate 1 -i images/%05d.png -c:v libx264 -preset ultrafast -qp 0 subtitles.mp4
