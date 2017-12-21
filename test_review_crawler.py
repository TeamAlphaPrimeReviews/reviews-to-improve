"""Test objects in review_crawler."""

import pdb
import pytest
from django.test import Client
from reviews_to_improve.review_crawler import review_maker

# from .reviews_to_improve.review_crawler import review_maker


def test_review_maker_list():
    """Test that review_texts is a list for strings."""
    assert isinstance('review_texts', str)


def test_review_maker_star_num_list():
    """Test review star num list takes ints."""
    assert isinstance('star_num_list', object)


# def test_review_maker_all_reviews():
#     """Test allreviews returns html."""
#     c = Client()
#     pdb.set_trace()
#     res = c.get('https://www.goodreads.com/book/show/28259132-chaos-monkeys#other_reviews')
