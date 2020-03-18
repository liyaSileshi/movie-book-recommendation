import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer #histogram(array) representation of words
from sklearn.metrics.pairwise import cosine_similarity #to calculate the cosine_similarity
from sklearn import datasets

df = pd.read_csv('music.csv')
print(df.keys())
