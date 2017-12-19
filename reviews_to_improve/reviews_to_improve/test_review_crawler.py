"""Test objects in review_crawler."""

import pytest


def test_review_maker_list():
    """Test that review_texts is a list."""
    from review_crawler import review_maker
    assert isinstance(review_texts, list)
