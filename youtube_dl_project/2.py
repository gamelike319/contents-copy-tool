import yt_dlp
import os
from pydub import AudioSegment

def download_audio_as_mp3_yt_dlp(url, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 音声のみダウンロードオプション
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("ダウンロードとMP3変換が完了しました。")

if __name__ == "__main__":
    url = input("ダウンロードしたいYouTubeのURLを入力してください: ")
    download_audio_as_mp3_yt_dlp(url)