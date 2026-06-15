#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
from pathlib import Path

def check_dependencies():
    """Ensure yt-dlp and ffmpeg are installed."""
    try:
        import yt_dlp
    except ImportError:
        print("yt-dlp not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "yt-dlp", "--break-system-packages"], check=True)
        import yt_dlp

    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except FileNotFoundError:
        print("ffmpeg not found! Please run: sudo apt-get update && sudo apt-get install -y ffmpeg")
        sys.exit(1)

def download_media(url, output_dir, extract_audio=False, extract_frames=False, frame_rate=1):
    import yt_dlp
    
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    outtmpl = str(out_dir / '%(title)s.%(ext)s')
    
    ydl_opts = {
        'outtmpl': outtmpl,
        'quiet': False,
        'no_warnings': True,
    }
    
    if extract_audio:
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'

    print(f"Downloading media from: {url}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get('title', 'video')
        
        # Determine output file path
        if extract_audio:
            media_path = out_dir / f"{title}.mp3"
        else:
            media_path = out_dir / f"{title}.mp4"
            
        print(f"Successfully downloaded to: {media_path}")

    # Extract frames if requested and we downloaded video
    if extract_frames and not extract_audio:
        print(f"Extracting frames at 1 frame every {frame_rate} second(s)...")
        frames_dir = out_dir / f"{title}_frames"
        frames_dir.mkdir(exist_ok=True)
        
        cmd = [
            "ffmpeg", "-i", str(media_path),
            "-vf", f"fps=1/{frame_rate}",
            str(frames_dir / "frame_%04d.jpg")
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Frames extracted to: {frames_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jules Utility: YouTube Downloader and Processor")
    parser.add_argument("url", help="YouTube URL to download")
    parser.add_argument("--outdir", default="output/temp_media", help="Output directory")
    parser.add_argument("--audio-only", action="store_true", help="Extract audio as MP3")
    parser.add_argument("--extract-frames", action="store_true", help="Extract video frames (requires video download)")
    parser.add_argument("--frame-rate", type=int, default=5, help="Extract 1 frame every N seconds")
    
    args = parser.parse_args()
    
    check_dependencies()
    download_media(args.url, args.outdir, args.audio_only, args.extract_frames, args.frame_rate)
