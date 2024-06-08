import os
import time
import psutil
from pytube import YouTube
from pydub import AudioSegment
from concurrent.futures import ProcessPoolExecutor
from typing import List, Optional

def download_youtube_as_mp3(url: str, output_path: str) -> Optional[str]:
    """Download a YouTube video and convert it to MP3 format."""
    try:
        # Create YouTube object
        yt = YouTube(url)
        
        # Filter for audio streams
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Download audio stream
        download_path = audio_stream.download(output_path=output_path)
        
        # Convert to MP3
        base, ext = os.path.splitext(download_path)
        mp3_path = base + '.mp3'
        
        audio = AudioSegment.from_file(download_path)
        audio.export(mp3_path, format="mp3")
        
        # Remove original file
        os.remove(download_path)
        
        print(f"Downloaded and converted: {mp3_path}")
        return mp3_path
    except Exception as e:
        print(f"An error occurred with URL {url}: {e}")
        return None

def download_from_file(file_path: str, output_path: str, max_workers: int = 4) -> None:
    """Download and convert multiple YouTube videos to MP3 format from a list of URLs."""
    with open(file_path, 'r', encoding='utf-8') as file:
        urls: List[str] = [url.strip() for url in file if url.strip()]

    # Using ProcessPoolExecutor for parallel downloads
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_youtube_as_mp3, url, output_path) for url in urls]
        
        # Wait for all the tasks to complete
        for future in futures:
            future.result()  # This will also raise any exceptions encountered during the download

if __name__ == "__main__":
    import multiprocessing
    file_path = 'urls.txt'  # Replace with the path to your text file containing URLs
    output_path = 'mp3'  # Replace with your desired output path
    max_workers = 4  # Adjust this based on the number of CPU cores you want to use

    print(f"CPU count: {multiprocessing.cpu_count()}")
    print(f"Max workers: {max_workers}")

    # Start a thread to monitor CPU and memory usage
    def monitor_usage():
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            memory_percent = memory_info.percent
            print(f"CPU usage: {cpu_percent}%")
            print(f"Memory usage: {memory_percent}%")
            time.sleep(1)

    import threading
    monitor_thread = threading.Thread(target=monitor_usage)
    monitor_thread.daemon = True
    monitor_thread.start()

    download_from_file(file_path, output_path, max_workers)
