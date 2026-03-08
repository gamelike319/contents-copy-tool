import os
import img2pdf
import glob
from datetime import datetime

# --- 設定 ---
TARGET_DIR = "captured_pages" # 画像があるフォルダ
# ------------

def make_pdf_only():
    # フォルダ内のpngファイルを取得して名前順にソート
    # page_0001.png, page_0002.png... となっているので単純ソートでOK
    image_files = sorted(glob.glob(os.path.join(TARGET_DIR, "*.png")))

    if not image_files:
        print(f"エラー: {TARGET_DIR} に画像が見つかりません。")
        return

    print(f"{len(image_files)} 枚の画像が見つかりました。PDF化します...")

    # 現在時刻でファイル名生成（ロック回避）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_name = f"recovered_book_{timestamp}.pdf"

    try:
        with open(pdf_name, "wb") as f:
            f.write(img2pdf.convert(image_files))
        print(f"成功！作成されたファイル: {pdf_name}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    make_pdf_only()