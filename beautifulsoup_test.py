"""Test of Beautiful Soup."""

from bs4 import BeautifulSoup
from datetime import datetime
import requests 



request = requests.get('https://www.goodreads.com/book/show/28259132-chaos-monkeys#other_reviews')

#request.content is where it's at

##page = urllib2.urlopen(request)
soup = BeautifulSoup(request.content, 'html.parser')
soup = soup.encode("utf-8")

import pdb; pdb.set_trace()
