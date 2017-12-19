"""Format requests from GoodReads website with Beautiful Soup."""

from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re
import pdb



# def request_maker():
#     """."""
#     run for loop over the url
#     add those to a list:


def review_maker():
    """Parse request from GoodReads website with BS."""
    review_texts = []
    star_num_list = []

    for i in range(1, 949):
        request = requests.get('https://www.rottentomatoes.com/m/star_wars_the_last_jedi/reviews/?page=%d&type=user&sort=' % i)

        soup = BeautifulSoup(request.content, 'html.parser')

        all_reviews = soup.find_all(class_="user_review")

        for text in all_reviews:
            # review = text.find_all('class_', id=lambda val: val and val.startswith('user_review'))
            review = text.get_text()
            review_texts.append(review)

        for star in all_reviews:
            num_stars = star.find(class_='scoreWrapper')
            pdb.set_trace()
            star_num_list.append(num_stars)
