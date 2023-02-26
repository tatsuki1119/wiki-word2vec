import glob
import logging
import os

import MeCab

if not os.path.exists("./wakati"):  # ディレクトリが無かったら作成
    os.mkdir("wakati")


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

tagger = MeCab.Tagger("-Owakati")

AllData = ''
Folders = glob.glob('text\*')  # textディレクトリ内のフォルダを取得


start_num = 0  # 開始するフォルダの番号を指定
# 一度で実行する場合は0,途中で止まった後に再開するときはその番号

f = open(f"wakati/wiki_data_{Folders[start_num][5:7]}.txt", 'r', encoding='UTF-8')  # 読み込むので"r",UTF-8を指定
AllData = f.read()


for FolderName in Folders[start_num+1:]:
    files = glob.glob(f"{FolderName}\*")  # フォルダの中身を取得
    for file in files:
        f = open(file, 'r', encoding='UTF-8')  # 読み込むので"r",UTF-8を指定
        data = f.read()
        #AllData += data + '\n'
        wakatiData = tagger.parse(data)
        AllData += wakatiData + '\n'
        logger.info(file)
        f.close()

    #wf = open(f'data/wiki_data_{FolderName[5:7]}.txt', 'w', encoding='UTF-8')
    wf = open(f'wakati/wiki_data_{FolderName[5:7]}.txt', 'w', encoding='UTF-8')
    wf.write(AllData)
    wf.close

wf = open('wiki_data.txt', 'w', encoding='UTF-8')
wf.write(AllData)
wf.close()
