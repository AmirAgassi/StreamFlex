# StreamFlex: Low-Impact Multi-Stream Automation

StreamFlex is a powerful Python-based automation tool designed for content creators and streamers who seek to maximize their reach while minimizing system and network load. This innovative script enables the streaming of a single pre-rendered video to multiple platforms simultaneously, employing a low-quality output to ensure efficiency.

## Features

- **Pre-Rendering for Efficiency**: StreamFlex pre-renders your videos to a lower quality using `ffmpeg`, significantly reducing CPU and bandwidth requirements during live streams.
- **Multi-Platform Streaming**: Originally configured for Twitch through RTMP, the script is versatile and can be adapted for use with other streaming services.
- **Automated Streaming and Break Intervals**: Features randomized streaming and break intervals to simulate live streaming, making it ideal for 24/7 channel management.
- **Low System Impact**: By optimizing video quality and streaming parameters, StreamFlex ensures minimal impact on system resources, allowing for smooth operation of other applications.
- **Concurrent Streaming**: Utilizes threading to support streaming to multiple keys/sources concurrently, perfect for content creators aiming to broadcast across various channels at once.
- **Easy Configuration**: Stream keys are easily managed through a simple text file, streamlining the setup process for users with multiple streaming accounts.

## How it Works

1. **Pre-Rendering**: Converts your high-quality video into a stream-friendly format, balancing quality and performance.
2. **Automated Streaming**: Leverages `ffmpeg` for continuous looping and streaming, with randomized intervals to mimic live broadcasting.
3. **Efficient Break Management**: Implements break periods between streams to further reduce system usage and mimic human-operated channel activity.

## Setup and Usage

1. Install `ffmpeg` on your system.
2. Place your video file in the same directory as StreamFlex and name it `Video.mp4` (or update the script with your video file's name).
3. Add your stream keys to `stream_keys.txt`, one per line.
4. Run the script. It will pre-render your video and start streaming based on the configured keys.

## Adaptability

While StreamFlex is pre-configured for Twitch, it can be easily modified for use with other streaming services that support RTMP. Adjust the `stream_cmd` variable to match the requirements of your preferred platform.

## Requirements

- Python 3.x
- `ffmpeg` installed and accessible from your system's PATH
- Internet connection capable of handling multiple video streams

## Disclaimer

StreamFlex is intended for use within the terms of service of the streaming platforms it interacts with. Users are responsible for ensuring their use of the script complies with these terms.

## Contributions

Contributions are welcome! Whether it's a feature enhancement, bug fix, or a guide on adapting StreamFlex for other platforms, your input helps make this tool better for everyone.

---
StreamFlex is the ultimate tool for content creators looking to efficiently manage their streaming presence across multiple platforms. With its focus on low-impact streaming and system efficiency, it represents a pivotal advancement in digital content management.
