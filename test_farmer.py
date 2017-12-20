"""To demonstrate tests of Jupyter notebook material."""

import pytest
from farmer import vocab_list
from farmer import vector_export    

def test_len_list():
    assert len(vocab_list) == 122

def test_len_item():
    assert vocab_list[0] == 'help'

def test_vector_help():
    assert vector_export['help'] == 45

def test_addition():
    assert vector_export['addition'] == 0

def test_len_vector_vocab():
    assert len(vector_export) == 116
