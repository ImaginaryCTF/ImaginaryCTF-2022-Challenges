#!/bin/bash

rm -rf output_images
mkdir output_images
ffmpeg -i subtitles.mp4 'output_images/%05d.png'

python3 solve.py
