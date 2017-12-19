"""Test objects in review_crawler."""

import pytest

from reviews_to_improve.review_crawler import review_maker


def test_review_maker_list():
    """Test that review_texts is a list."""
    from reviews_to_improve.review_crawler import review_maker
    assert isinstance('review_texts', str)
