from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re
import pdb


request = requests.get('https://www.goodreads.com/book/show/28259132-chaos-monkeys#other_reviews')

#request.content is where it's at

##page = urllib2.urlopen(request)
soup = BeautifulSoup(request.content, 'html.parser')

review_texts = []
stars_text = []

all_reviews = soup.find_all(class_="friendReviews")

for text in all_reviews:
    review = text.find_all('span', id=lambda val: val and val.startswith('freeTextContainer'))[0].string
    review_texts.append(review)

for star in all_reviews:
    number_stars = len(star.find(class_='staticStars').find_all(class_='p10'))
    stars_text.append(star)
