from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('./wiki_tag_removed_data.txt')

model = word2vec.Word2Vec(sentences, vector_size=200, min_count=20, window=15)
model.wv.save_word2vec_format("./wiki.model", binary=True)
