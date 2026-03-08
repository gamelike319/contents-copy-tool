import yt_dlp
import os
# from pydub import AudioSegment  # 今回のサンプルでは使用しません（不要なら削除可）

def download_video_yt_dlp(url, output_path="downloads"):
    """
    YouTubeから動画をダウンロードする
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 動画と音声の最適（best）をマージ
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("動画ダウンロードが完了しました。")

def download_audio_as_mp3_yt_dlp(url, output_path="downloads"):
    """
    YouTubeから音声のみ(MP3)をダウンロードする
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # 音声のみダウンロード＆MP3変換のオプション
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

    print("音声ダウンロードとMP3変換が完了しました。")

def main():
    url = input("ダウンロードしたいYouTubeのURLを入力してください: ")
    choice = input("ダウンロードモードを選択してください [1:動画, 2:音声(MP3)] : ")

    if choice == "1":
        download_video_yt_dlp(url)
    elif choice == "2":
        download_audio_as_mp3_yt_dlp(url)
    else:
        print("不明な選択です。1 または 2 を選択してください。")

if __name__ == "__main__":
    main()
