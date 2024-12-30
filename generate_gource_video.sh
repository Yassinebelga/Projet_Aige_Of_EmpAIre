#!/bin/bash

# Check if the user provided an argument for the output video name
if [ -z "$1" ]; then
  echo "Usage: $0 <output_video_name>"
  exit 1
fi

# Get the date of the last commit
LAST_COMMIT_DATE=$(git log -1 --format=%cd --date=format:'%Y-%m-%d')

# Append the last commit date to the output video name
OUTPUT_VIDEO="${1}_${LAST_COMMIT_DATE}.mp4"

# Generate the Gource visualization and convert it to a video
gource -1280x720 --seconds-per-day 0.1 -o gource_output.ppm
ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i gource_output.ppm -vcodec libx264 "$OUTPUT_VIDEO"

# Clean up the temporary PPM file
rm gource_output.ppm

echo "Gource video saved as $OUTPUT_VIDEO"

