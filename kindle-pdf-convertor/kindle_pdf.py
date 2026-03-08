import pyautogui
import time
import os
import img2pdf
from datetime import datetime
from PIL import Image, ImageChops # 画像比較用

# --- 設定エリア ---
PAGE_TURN_WAIT = 1.0  # 読み込み時間を考慮して少し長めに
OUTPUT_DIR = "captured_pages"
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
PDF_NAME = f"kindle_book_{TIMESTAMP}.pdf"
# -----------------

def create_folder():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def capture_auto_stop():
    print("5秒後に開始します。Kindleを最大化してください...")
    time.sleep(5)

    captured_files = []
    page_count = 0
    prev_image = None # 比較用の前ページ画像

    while True:
        # ファイル名
        page_count += 1
        filename = os.path.join(OUTPUT_DIR, f"page_{page_count:04d}.png")
        
        # スクリーンショット撮影
        # メモリ上で画像を取得（ファイル保存は後）
        current_image = pyautogui.screenshot()
        
        # --- 終了判定ロジック ---
        if prev_image is not None:
            # 差分を取得
            diff = ImageChops.difference(current_image, prev_image)
            # 差分があるバウンディングボックスを取得（完全に一致ならNone）
            if diff.getbbox() is None:
                print(f"ページ変化なし（最終ページ到達と判断）。処理を終了します。")
                break
        # ----------------------

        # 画像を保存
        current_image.save(filename)
        captured_files.append(filename)
        print(f"保存完了: {filename} ({page_count}ページ目)")

        # 現在の画像を「前回の画像」として保持
        prev_image = current_image

        # 次のページへ
        pyautogui.press('left') 
        time.sleep(PAGE_TURN_WAIT)

    return captured_files

def convert_to_pdf(image_files):
    if not image_files: return
    print("PDF作成中...")
    try:
        with open(PDF_NAME, "wb") as f:
            f.write(img2pdf.convert(image_files))
        print(f"完了: {PDF_NAME}")
    except Exception as e:
        print(f"PDF作成エラー: {e}")

if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    try:
        create_folder()
        images = capture_auto_stop()
        convert_to_pdf(images)
    except KeyboardInterrupt:
        print("\n中断しました。")