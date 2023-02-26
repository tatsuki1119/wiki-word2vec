from gensim.models import KeyedVectors

wv = KeyedVectors.load_word2vec_format('wiki.model', binary=True)

jpkr = wv.similarity('日本', '韓国')
print(f'日本と韓国の類似度 : {jpkr}')
