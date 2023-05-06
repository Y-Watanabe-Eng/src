import sys
import os
import win32com.client as win32
import subprocess
from time import sleep
import pyautogui
from PIL import ImageGrab


#ドラッグしたブックのパスを取得
filepath = sys.argv[1]

#ファイル名と拡張子を取得
filename = os.path.splitext(os.path.basename(filepath))[0]
ext = os.path.splitext(filepath)

#Excelに接続
xl = win32.Dispatch("Excel.Application")

#ブックを開く
wb = xl.Workbooks.Open(filepath)

#シートを指定
ws = wb.Worksheets(1)

#セル範囲を指定
range = ws.UsedRange

#指定した範囲をクリップボードにコピー
range.Copy()

#ペイントを起動
subprocess.Popen('mspaint')

#起動待機
sleep(1)

#ペースト⇒コピーで画像取得
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'x')

#ペイントを閉じる
pyautogui.hotkey('alt', 'f4')
pyautogui.hotkey('n')

#Excelを閉じる
wb.close

#クリップボードの内容を取得
img = ImageGrab.grabclipboard()

#Excelコピー時に入った左端と上端の1pxの線をトリミング
img = img.crop((1, 1, img.size[0], img.size[1]))

#保存フォルダを作成
if not os.path.exists('img'):
    os.makedirs('img')

#画像の保存先を指定
savepath = './img/' + filename + '.png'

#画像を保存
img.save(savepath)
