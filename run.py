import subprocess
import threading
import time
import random

video_file = "Video.mp4"

def pre_render_video():
    # Pre-render the video
    pre_render_cmd = [
        "ffmpeg", "-i", video_file,
        "-vcodec", "h264_nvenc", "-preset", "medium", "-profile:v", "main", "-rc:v", "vbr_hq",
        "-pix_fmt", "yuv420p", "-b:v", "1M", "-maxrate:v", "0.1M", "-bufsize:v", "2M",
        "-acodec", "aac", "-b:a", "128k", "-ar", "44100",
        "-f", "flv", "pre_rendered_video.flv"
    ]
 
    subprocess.run(pre_render_cmd)

def run_ffmpeg(stream_key):
    while True:
        try:
            # Random interval for streaming (3-9 hours in seconds)
            stream_duration = random.randint(3 * 3600, 9 * 3600)
            # Random interval for break (2-6 hours in seconds)
            break_duration = random.randint(2 * 3600, 6 * 3600)

            stream_cmd = [
                "ffmpeg", "-re", "-stream_loop", "-1", "-i", "pre_rendered_video.flv",
                "-c:v", "libx264", "-preset", "ultrafast", "-b:v", "1500k", "-g", "60", 
                "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
                "-f", "flv", f"rtmp://live-fra.twitch.tv/app/{stream_key}"
            ]

            # Run streaming command
            subprocess.run(stream_cmd, timeout=stream_duration)

            # Break interval
            time.sleep(break_duration)
        except:
            pass

# Pre-render the video
pre_render_video()

# Read stream keys from file
with open("stream_keys.txt", "r") as file:
    stream_keys = file.read().splitlines()

# Create and start threads for each stream key
threads = []
for key in stream_keys:
    thread = threading.Thread(target=run_ffmpeg, args=(key,))
    thread.start()
    threads.append(thread)