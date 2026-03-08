import yt_dlp
import os
import sys

# ダウンロード先ディレクトリの定義
OUTPUT_DIR = "downloads"

def run_download(url, ydl_opts, mode_name):
    """
    yt-dlpを使用したダウンロード実行とエラーハンドリングを行う共通関数
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print(f"\n--- {mode_name} のダウンロードを開始します ---")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✅ {mode_name} のダウンロードが完了しました。")
    except yt_dlp.utils.DownloadError as e:
        print(f"❌ ダウンロードに失敗しました ({mode_name})。")
        print("💡 解決策: YouTube側の変更が原因の可能性が高いです。")
        print("   まず、ターミナルで 'pip install -U yt-dlp' を実行し、yt-dlpを最新版に更新してください。")
        print(f"   詳細エラー: {e}")
    except Exception as e:
        print(f"❌ 予期せぬエラーが発生しました: {e}")

def download_video_yt_dlp(url):
    """
    YouTubeから動画をダウンロードする (bestvideo+bestaudioをMP4としてマージ)
    """
    # 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best'で、高画質のMP4と高音質のM4Aを選び、
    # FFmpegでMP4にマージすることを明示的に推奨します。
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best', 
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4', # 結合後のファイル形式を指定
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4', # マージにFFmpegを使用
        }],
    }
    run_download(url, ydl_opts, "動画 (MP4)")

def download_audio_as_mp3_yt_dlp(url):
    """
    YouTubeから音声のみ(MP3)をダウンロードする
    """
    # 音声のみダウンロード＆MP3変換のオプション
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # 注: MP3変換にはFFmpegが必要です
    }
    run_download(url, ydl_opts, "音声 (MP3)")

def main():
    print("--- YouTubeダウンローダー by yt-dlp ---")
    url = input("ダウンロードしたいYouTubeのURLを入力してください: ")

    # URLが空の場合は終了
    if not url:
        print("URLが入力されませんでした。終了します。")
        sys.exit()

    while True:
        choice = input("ダウンロードモードを選択してください [1:動画, 2:音声(MP3)] : ")
        if choice == "1":
            download_video_yt_dlp(url)
            break
        elif choice == "2":
            download_audio_as_mp3_yt_dlp(url)
            break
        else:
            print("❗ 不明な選択です。1 または 2 を入力してください。")

if __name__ == "__main__":
    main()