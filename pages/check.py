import os

file_path = './data/quiz_1.csv'

if os.path.exists(file_path):
    print("ファイルが存在します")
else:
    print("ファイルが存在しません")

print("カレントディレクトリ:", os.getcwd())

# 現在のスクリプトのファイルパスを取得
current_file_path = __file__

# ファイルのディレクトリパスを取得
current_directory = os.path.dirname(current_file_path)

print(f"現在のファイルのディレクトリ: {current_directory}")