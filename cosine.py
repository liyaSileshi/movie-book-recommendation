
from sklearn.feature_extraction.text import CountVectorizer #histogram(array) representation of words
from sklearn.metrics.pairwise import cosine_similarity #to calculate the cosine_similarity

text = ['London Paris London', 'Paris Paris London']

cv = CountVectorizer()
count_matrix = cv.fit_transform(text)
print(cv.get_feature_names())
# print(count_matrix.toarray())
similarity_scores = cosine_similarity(count_matrix)
print(similarity_scores)