import pytest

from utils.words import EnglishWords


@pytest.fixture
def english_words():
    return EnglishWords()


@pytest.fixture(params=['zebra', 'lion', 'goliath', 'maccaroni'])
def english_word_example(request):
    return request.param
