"""Format requests from GoodReads website with Beautiful Soup."""

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re
import pdb


def review_maker():
    """Parse request from GoodReads website with BS."""
    review_texts = []
    star_num_list = []

    for i in range(1, 9):
        request = requests.get('https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?page=%d&type=user&sort=' % i)
        if request.status_code == 200:

            soup = BeautifulSoup(request.content, 'html.parser')

            all_reviews = soup.find_all(class_="user_review")

            for text in all_reviews:
                review = text.get_text()
                review_texts.append(review)

            for star in all_reviews:
                num_stars = star.find(class_='scoreWrapper').span['class'][0]
                star_num_list.append(num_stars)
    pdb.set_trace()
