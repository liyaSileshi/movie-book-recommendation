import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer #histogram(array) representation of words
from sklearn.metrics.pairwise import cosine_similarity #to calculate the cosine_similarity
from sklearn import datasets


df = pd.read_csv('movie_dataset.csv')

# print(df.keys()) #gives all the attributes in the dataset

features = ["keywords","cast","genres","director"] #columns we care about

def combine_features(row):
    '''combines the values of the columns into 1 string'''
    return row['keywords']+' '+row['cast']+' '+row['genres']+' '+row['director']

for feature in features:
    df[feature] = df[feature].fillna(' ') #filling all NaNs with blank string


#applying combined_features() method over each rows of dataframe 
#and storing the combined string in “combined_features” column
df["combined_features"] = df.apply(combine_features,axis=1)

cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df['combined_features']) #feeding combined strings(movie contents) to CountVectorizer() object
cosine_sim = cosine_similarity(count_matrix)
# print(cosine_sim)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]

movie_user_likes = 'Avatar'
movie_index = get_index_from_title(movie_user_likes)

#accessing the row corresponding to given movie to find
# all the similarity scores for that movie and then enumerating over it
similar_movies = list(enumerate(cosine_sim[movie_index])) #tuple (index,similarity)

#sorting the movies by their similarity (second index in the tuple)
sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]


i = 0
for element in sorted_similar_movies:
        print(get_title_from_index(element[0])) #element[0] gives us index of the movie
        i += 1
        if i > 5:
            break