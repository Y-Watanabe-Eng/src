import os
import winshell
import subprocess
from time import sleep

#フォルダ指定
folder_path = './Start'

#相対パスを絶対パスに変換
abs_folder_path = os.path.abspath(folder_path)

#フォルダの有無をチェック
if not os.path.exists(folder_path):
    #フォルダがない場合は作成
    os.makedirs(folder_path)
    #併せてサンプルテキストを作成
    text = open('./Start/sample.txt','w')
    #テキスト編集
    text.write('ご利用ありがとうございます。\
        \nStartフォルダを作成しましたので、\
        \n起動したいファイル、ショートカット等を格納し、\
        \n再度、Start.exeを実行してください。')
    text.close()
    #作成したフォルダを開く
    subprocess.Popen(['explorer', abs_folder_path], shell=True)
    #起動待ち
    sleep(1)

#フォルダ内のファイルを取得
files = [f for f in os.listdir(abs_folder_path)]

#順番にファイルを開く
for file in files:
    file_path = os.path.join(abs_folder_path, file)
    shortcut = winshell.shortcut(file_path)
    shortcut_path = shortcut.path
    os.startfile(shortcut_path)