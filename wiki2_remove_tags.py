import re

import MeCab


f = open("wiki_data.txt", 'r', encoding='UTF-8')
data = f.read()
f.close()


# 最初にあるタグを消す
data = re.sub(r"<.*?>", r"", data)
# 半角記号削除
data = re.sub(r'[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]', '', data)
# 全角記号削除
data = re.sub("[\uFF01-\uFF0F\uFF1A-\uFF20\uFF3B-\uFF40\uFF5B-\uFF65\u3000-\u303F]", '', data)

# print(data[0:10000])

# ファイルに書き込み
wf = open('wiki_tag_removed_data.txt', 'w', encoding='UTF-8')
wf.write(data)
wf.close()
