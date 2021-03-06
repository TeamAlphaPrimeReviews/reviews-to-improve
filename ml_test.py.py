"""Machine Learning Building."""


import nltk
import pandas as pd
import psycopg2

nltk.download()

conn = psycopg2.connect

data = pd.read_csv("sw_good.csv")

#print("Total rows: {0}".format(len(data)))

#print(list(data))

bad_reviews = data[data.good_or_bad == 'Bad']

print(bad_reviews.loc['Review', : ])