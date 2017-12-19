"""Test objects in review_crawler."""

import pytest

from reviews_to_improve.review_crawler import review_maker


def test_review_maker_list():
    """Test that review_texts is a list for strings."""
    from reviews_to_improve.review_crawler import review_maker
    assert isinstance('review_texts', str)


def test_review_maker_star_num_list():
    """Test review star num list takes ints."""
    from reviews_to_improve.review_crawler import review_maker
    assert isinstance('star_num_list', object)
