import pytest

from wordle_interface import WordleInterface
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


@pytest.fixture
def interface():
    return WordleInterface()


@pytest.fixture(params=['karmkergaergrreg', 12334, True, ValueError, '', '234', 'aa', 'AKFV'])
def invalid_interface_guess(request):
    return request.param
