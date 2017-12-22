"""Test objects in review_crawler."""
from review_crawler import review_maker

reviews = review_maker()


def test_review_maker_list():
    """Test that review_texts is a list for strings."""

    assert isinstance(reviews, set)


def test_review_maker_lst_contains_instance_of_tuple():
    """Test that a list version of the set returned from review_maker contains
    tuples."""

    review_lst = list(reviews)
    assert isinstance(review_lst[0], tuple)


def test_review_maker_lst_has_value_that_can_be_integerized():
    """Test that the lst of the review set contains a tuple that has a value
    that is a string representation of an integer."""
    review_lst = list(reviews)
    assert isinstance(int(review_lst[0][1]), int)


def test_review_maker_lst_has_string_value():
    """Test that the lst of the review set contains a tuple that has a string
    value."""
    review_lst = list(reviews)
    assert isinstance(str(review_lst[0][0])d, str)


# def test_review_maker_all_reviews():
#     """Test allreviews returns html."""
#     c = Client()
#     pdb.set_trace()
#     res = c.get('https://www.goodreads.com/book/show/28259132-chaos-monkeys#other_reviews')
