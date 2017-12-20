
import nltk

import pandas as pd


# In[3]:


data = pd.read_csv("sw_good.csv")


# In[13]:


import sklearn.feature_extraction.text


# In[4]:


from nltk.tokenize import word_tokenize


# In[5]:


import scipy


# In[6]:


import string


# In[7]:


from nltk.corpus import stopwords


# In[16]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[17]:


vectorizer = TfidfVectorizer()


# In[43]:


data


# In[22]:


vocab_list = []


# In[ ]:


"""Prepare the text for analysis."""


# In[32]:


for item in data['Review']:   
    # split into words
    tokens = word_tokenize(item)
    # convert to lowercase
    tokens = [w.lower() for w in tokens]
    # remove punctuation and abberations
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    # words is now a list of the significant words
    for word in words:
        vocab_list.append(word)
    
      


# In[33]:


print(len(vocab_list))


# In[37]:


print(vocab_list[0])


# In[ ]:


# Fitting the list


# In[38]:

"""
In Jupyter notebook the fitting had to be done to vocab_list[0] but 
it gives me an error in Python when I try to use it that way.
"""

vectorizer.fit(vocab_list)


# In[41]:


# Summarize


# In[39]:


print(vectorizer.vocabulary_)
vector_export = vectorizer.vocabulary_
print(len(vector_export))
# In[44]:


#print(len(vectorizer.vocabulary_))


# In[40]:


#vector = vectorizer.transform()

