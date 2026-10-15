#!/usr/bin/env bash
# The final files of a cut: picture from render.js, sound from mix.py.
#   tools/encode.sh ar   →  out/masahif-al-maghrib-ar.mp4 (1080×1920, for upload)
#                           out/masahif-al-maghrib-ar-whatsapp.mp4 (720×1280, light)
set -euo pipefail
cd "$(dirname "$0")/.."
lang=$1
pic=build/$lang/video.mp4
snd=build/$lang/mix.wav
mkdir -p out
if [ "$lang" = ar ]; then
  title="مصاحف المغرب · masahif-al-maghrib.com"
  credit="تطوير الموقع وإنتاج الفيديو: خالد بن جلون، مطوّر من فاس"
  alang=ara
else
  title="Masahif al-Maghrib · masahif-al-maghrib.com"
  credit="Website development and video production: Khalid Benjelloun, developer from Fez"
  alang=eng
fi
meta=(-metadata "title=$title" -metadata "comment=$credit" -metadata "artist=Khalid Benjelloun"
      -metadata:s:a:0 "language=$alang")

# for Reels, Shorts, TikTok, Facebook, X: full size, generous bitrate
ffmpeg -y -v error -i "$pic" -i "$snd" -map 0:v -map 1:a \
  -c:v libx264 -preset slow -crf 19 -maxrate 9M -bufsize 18M -pix_fmt yuv420p -profile:v high -level 4.2 \
  -g 60 -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -b:a 192k -ar 48000 -movflags +faststart "${meta[@]}" "out/masahif-al-maghrib-$lang.mp4"

# for WhatsApp and Telegram: 720p, small enough to send as a video
ffmpeg -y -v error -i "$pic" -i "$snd" -map 0:v -map 1:a \
  -vf "scale=720:1280:flags=lanczos" -c:v libx264 -preset slow -b:v 1700k -maxrate 2400k -bufsize 4800k \
  -pix_fmt yuv420p -profile:v high -level 4.0 -g 60 -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -b:a 128k -ar 48000 -movflags +faststart "${meta[@]}" "out/masahif-al-maghrib-$lang-whatsapp.mp4"

# a cover frame for the platforms that ask for one: the name of the guide, just revealed
t=$(python3 -c "import json; d=json.load(open('scene/timeline.$lang.json', encoding='utf-8')); print(d['segments'][3]['speechEnd'] + 0.55)")
ffmpeg -y -v error -ss "$t" -i "$pic" -frames:v 1 -q:v 2 "out/cover-$lang.jpg"

ls -la out/masahif-al-maghrib-"$lang"*.mp4 "out/cover-$lang.jpg"
