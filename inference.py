from numpy import dot
import numpy as np
import pandas as pd
from numpy.linalg import norm
from gensim.models import Word2Vec
from gensim.models import FastText
from modular_code.ML_pipeline import textprocess

text_clean = textprocess.Text_cleaning()


class Medical_Inference:
    def __init__(self):
        self.data = pd.read_csv('inputs/Dimension-covid.csv')

    def get_mean_vector(self, model, words):
        # remove out-of-vocabulary words
        words = [word for word in text_clean.tokenize(words) if
                 word in list(model.wv.index_to_key)]  # if word is in vocab
        if len(words) >= 1:
            return np.mean(model.wv[words], axis=0)
        else:
            return np.array([0] * 100)

    def cos_sim(self, a, b):
        return dot(a, b) / (norm(a) * norm(b))

    def preprocessing_input(self, query, model):
        query = text_clean.preprocessing(self.data, text=query)
        query = query.replace('\n', ' ')
        K = self.get_mean_vector(model, query)
        return K

    def top_n(self, query, p, data, model):
        x = []
        query = self.preprocessing_input(query, model)  # preprocessing input to list of vectors x=[]
        # Converting cosine similarities of overall data set with input queries into LIST
        for i in range(len(p)):
            x.append(self.cos_sim(query, p[i]))

        # store list in tmp to retrieve index
        tmp = list(x)

        # sort list so that largest elements are on the far right

        res = sorted(range(len(x)), key=lambda sub: x[sub])[-5:]
        sim = [tmp[i] for i in reversed(res)]
        # get index of the 10 or n largest element
        L = []
        for i in reversed(res):
            L.append(i)
        return data.iloc[L, [1, 2, 3, 4, 5, 6, 7]], sim  # returning dataframe (only id,title,abstract ,publication date)

def main():
    fasttext_vectors = np.load('models/fast_vectors.npy')
    inference = Medical_Inference()
    data = pd.read_csv('inputs/Dimension-covid.csv')
    FastText = Word2Vec.load('models/FastText.bin')
    data, sim = inference.top_n('lung failure', fasttext_vectors, data, FastText)
    print(data, sim)

if __name__=='__main__':
    main()