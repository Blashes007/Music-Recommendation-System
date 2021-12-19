import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Song_ratings = pd.read_csv('song_data.csv')

Song_ratings.head()

Song_ratings.drop(['release','year'],1, inplace = True)
Song_ratings.head()

ratings = Song_ratings.pivot_table(index=['artist_name'],columns=['song_title'],values='reviews_rating')
ratings.head()
ratings = ratings.dropna(thresh=5, axis=1).fillna(0,axis=1)
ratings.shape
ratings.head()

correlation_matrix = ratings.corr(method='pearson')
correlation_matrix.head(100)

def get_same_song(song_title,rating):
    same_songs = correlation_matrix[song_title]*(rating-2.5)
    same_songs = same_songs.sort_values(ascending=False)
    return same_songs
get_same_song('Angel',5).head(10)
