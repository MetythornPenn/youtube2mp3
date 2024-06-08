# YouTube to MP3 Downloader

This project provides a script to download YouTube videos and convert them to MP3 format using multiple CPU cores for better performance. It also monitors CPU and memory usage during the download process.

## Features

- Download audio from YouTube videos and convert them to MP3.
- Process multiple URLs concurrently using multiple CPU cores.
- Monitor CPU and memory usage during the process.

## Requirements

- Python 3.6+
- `pytube` for downloading YouTube videos.
- `pydub` for audio conversion.
- `psutil` for monitoring system usage.
- `ffmpeg` or `libav` for audio processing (required by `pydub`).

## Installation

1. **Install Python packages**:

    ```sh
    pip install pytube pydub psutil
    ```

2. **Install ffmpeg**:
   
   On macOS using Homebrew:

    ```sh
    brew install ffmpeg
    ```

   On Ubuntu:

    ```sh
    sudo apt update
    sudo apt install ffmpeg
    ```

   On Windows, download the binaries from [ffmpeg.org](https://ffmpeg.org/download.html) and add them to your PATH.

## Usage

1. **Prepare a text file with YouTube URLs**:
   
   Create a text file (`urls.txt`) with each line containing a YouTube video URL you want to download.

2. **Run the script**:
   
   ```sh
   python main.py
