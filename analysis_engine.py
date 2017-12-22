
# coding: utf-8

# In[50]:


import csv


# In[51]:


import nltk


# In[52]:


import numpy as np


# In[53]:


import pandas as pd


# In[54]:


import sklearn.feature_extraction.text


# In[55]:


from sklearn.feature_extraction.text import CountVectorizer


# In[56]:


from sklearn.feature_extraction.text import TfidfTransformer


# In[57]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[58]:


from sklearn.naive_bayes import MultinomialNB


# In[59]:


from sklearn import metrics


# In[60]:


import scipy


# In[61]:


import string


# In[62]:


from nltk.tokenize import word_tokenize


# In[63]:


from nltk.corpus import stopwords


# In[64]:


#Opening the file


# In[200]:


the_data = pd.read_csv("all_reviews.csv")


# In[201]:


# Randomizing the rows in the file


# In[244]:


the_data = the_data.reindex(np.random.permutation(the_data.index))


# In[245]:


# Total instances in the csv data, pre-sorting into train and test.
good = 0
bad = 0
for item in the_data['good/bad']:
    if item == 'bad':
        bad += 1
    if item == 'good':
        good += 1
print('Good: ' + str(good))
print('Bad: ' + str(bad))
        


# In[246]:


data = []
for index, row in the_data.iterrows():
    sentence = ""
    # extract the review from the original
    review = str(row['review'])
    # split into words
    tokens = word_tokenize(review)
    # convert to lowercase
    tokens = [w.lower() for w in tokens]
    # remove punctuation and abberations
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words & join in a sentence
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w not in stop_words]
    sentence = ' '.join(words)
    data.append({'stars': (row['stars']) / 10,
                      'review': sentence,
                      'good/bad': row['good/bad']})
new_frame = pd.DataFrame(data)


# In[247]:


# Create a new dataframe with modified star value & a cleaned up review


# In[248]:


#Extracting features from text, define target y and data x


# In[249]:


X = new_frame['review']
Y = new_frame['good/bad']


# In[250]:


#Partitioning the data into test and training set
split = 0.75
split_size = int(len(new_frame)*split)

X_train = X[:split_size]
X_test = X[split_size:]

Y_train = Y[:split_size]
Y_test = Y[split_size:]


# In[251]:


vect = CountVectorizer()


# In[252]:


X_train_dtm = vect.fit_transform(X_train)


# In[253]:


tfidf_transformer = TfidfTransformer()


# In[254]:


X_train_tfidf = tfidf_transformer.fit_transform(X_train_dtm)


# In[314]:


X_train_tfidf


# In[255]:


# -------------------------------------------------


# In[256]:


X_test_dtm = vect.transform(X_test)


# In[257]:


X_test_tfidf = tfidf_transformer.transform(X_test_dtm)


# In[315]:


X_test_tfidf


# In[258]:


#Test data numbers
test_good = 0
test_bad = 0 

for rating in Y_test:
    if rating == 'good':
        test_good += 1
    if rating == 'bad':
        test_bad += 1
print('Good reviews in test data: ' + str(test_good))
print('Bad reviews in test data: ' + str(test_bad))


# In[259]:


# Training the model


# In[260]:


clf = MultinomialNB()
clf.fit(X_train_tfidf, Y_train)


# In[261]:


# Evaluating the results


# In[262]:


# Accuracy on training set
clf.score(X_train_tfidf, Y_train)


# In[263]:


# Accuracy on testing set
print(clf.score(X_test_tfidf, Y_test))


# In[264]:


Y_pred = clf.predict(X_test_tfidf)
print(metrics.classification_report(Y_test, Y_pred))


# In[265]:


# False negative
X_test[Y_pred > Y_test]


# In[266]:


#Messing around to see what we can pull.


# In[267]:


# Testing it on new data


# In[290]:


test = ['SJW bullshit']


# In[291]:


t_test = vect.transform(test)


# In[292]:


y_pred = clf.predict(t_test)


# In[293]:


print(y_pred)


# In[294]:


# Predicting quality of unsorted data


# In[295]:


#Importing
feature_data = pd.read_csv("test2.csv")


# In[296]:


# This is to test the data is importing correctly
feature_good = 0
feature_bad = 0
for item in feature_data['stars']:
    if item >= 25:
        feature_good += 1
    else:
        feature_bad += 1
print('Positive Reviews: ' + str(feature_good))
print('Negative Reviews: ' + str(feature_bad))


# In[297]:


# Cleaning
feature_list = []
for index, row in feature_data.iterrows():
    sentence = ""
    # extract the review from the original
    review = row['review']
    # split into words
    tokens = word_tokenize(review)
    # convert to lowercase
    tokens = [w.lower() for w in tokens]
    # remove punctuation and abberations
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words & join in a sentence
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w not in stop_words]
    sentence = ' '.join(words)
    feature_list.append({'stars': (row['stars']) / 10,
                      'review': sentence,
                      'good/bad': row['good/bad']})
feature_frame = pd.DataFrame(feature_list)


# In[298]:


feature_counts = vect.transform(feature_frame['review'])


# In[299]:


feature_counts


# In[302]:


feature_test = vect.transform(feature_frame)


# In[304]:


feature_counts = vect.transform(feature_frame['review'])


# In[305]:


new_y_pred = clf.predict(feature_counts)


# In[306]:


feature_good = 0
feature_bad = 0
for i in new_y_pred:
    if i == 'good':
        feature_good += 1
    if i == 'bad':
        feature_bad += 1


# In[307]:


print("Bad: " + str(feature_bad) + " Good: " + str(feature_good))


# In[281]:


# -------------------------------------------------------------- #


# In[308]:


X_train_tokens = vect.get_feature_names()
len(X_train_tokens)


# In[309]:


a_token = clf.feature_count_[0, :]
b_token = clf.feature_count_[1, :]
tokens = pd.DataFrame({'token': X_train_tokens, 'bad': a_token, 'good': b_token}).set_index('token')


# In[310]:


tokens.head()


# In[311]:


tokens['bad'] += 1
tokens['good'] += 1
tokens.sample(5, random_state=6)


# In[312]:


tokens['ratio'] = tokens.bad / tokens.good
tokens.sample(5, random_state=6)


# In[313]:


tokens.sort_values('ratio', ascending=False)

