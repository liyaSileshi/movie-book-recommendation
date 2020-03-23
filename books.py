import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer #histogram(array) representation of words
from sklearn.metrics.pairwise import cosine_similarity #to calculate the cosine_similarity
from sklearn import datasets
from scipy import sparse
import json

#data from goodbooks-10k dataset
df = pd.read_csv('book_detail.csv')
df.drop(df.columns[[-1,-6,-7]], axis=1, inplace=True) #delete these column

df.drop(df[df['genre']==''].index, inplace=True)

df = df[df['genre'].notna()] #drop the NaN rows in column 'genre'
# get the values from the genre column json object and append to a list
genres = []
for i in df['genre']:
    genres.append(list(json.loads(i).values()))
    
# assign it to a new column
df['genre_new'] = genres

#drop the genre column
df.drop(df.columns[[-2]], axis=1, inplace=True)

#clean the year column
df['year'] = df['year'].str[:4] #keep only the year

features = ["author","genre_new","year"] #columns we care about
for feature in features:
    df[feature] = df[feature].fillna(' ') #filling all NaNs with blank string

#make a new column named genre that holds the string version of genre_new col of type list
df['genre'] = [' '.join(map(str, l)) for l in df['genre_new']] 

df = df.reset_index(drop=True) #resetting the index numbers

def combine_features(row):
    '''combines the values of the columns into 1 string'''
    return row['author']+' '+row['genre']+' '+row['year']

#applying combined_features() method over each rows of dataframe 
#and storing the combined string in “combined_features” column
df["combined_features"] = df.apply(combine_features,axis=1)

df['index'] = df.index #make a new column that holds the index 

cv = CountVectorizer() #creating new CountVectorizer() object
count_matrix = cv.fit_transform(df['combined_features']) #feeding combined strings(movie contents) to CountVectorizer() object
cosine_sim = cosine_similarity(count_matrix)

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
    try:
        return df[df.title == title]["index"].values[0]

    except IndexError:
        return f'No book with the name {title}'

def get_five_similar_books(book_user_likes):
    book_index = get_index_from_title(book_user_likes)
    if type(book_index) != np.int64: #check if book_index is not an int
        return f'No book with the name {book_user_likes}'

    #accessing the row corresponding to given movie to find
    # all the similarity scores for that movie and then enumerating over it
    similar_books = list(enumerate(cosine_sim[book_index])) #tuple (index,similarity)
    #sorting the books by their similarity (second index in the tuple) cosine
    sorted_similar_books = sorted(similar_books,key=lambda x:x[1],reverse=True)[1:]
    i = 0
    book_array = [] #create an empty list
    for element in sorted_similar_books:
            book_array.append(get_title_from_index(element[0])) #element[0] gives us index of the movie
            i += 1
            if i >= 5:
                break
    return book_array

if __name__ == '__main__':
    print(get_five_similar_books('abc'))