# 画面キャプチャ自動化ツール

## 概要
このスクリプトは、画面を一定間隔でキャプチャし、前回画像と比較しながら変化がなくなるまで保存を続け、最後に保存済み画像を PDF にまとめる Python ツールです。

## 主な機能
- 画面全体のスクリーンショットを自動取得
- 前回画像との差分比較による自動停止
- 連番 PNG 保存
- 複数画像の PDF 化

## 必要環境
- Python 3.x
- pyautogui
- Pillow
- img2pdf

## インストール
```bash
pip install pyautogui pillow img2pdf