import pytest

from utils.words import EnglishWords


@pytest.fixture
def english_words():
    return EnglishWords()


@pytest.fixture(params=['zebra', 'lion', 'goliath', 'maccaroni'])
def english_word_example(request):
    return request.param


@pytest.fixture(params=['', 'blabla'])
def fake_word_example(request):
    return request.param


@pytest.fixture(params=[0, 1, 2, 3, 5, 10])
def length(request):
    return request.param