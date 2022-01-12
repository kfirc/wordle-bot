from assertpy import assert_that

from utils.words import EnglishWords


class TestWords:
    def test_english_words_is_singleton(self):
        english_words_1 = EnglishWords()
        english_words_2 = EnglishWords()
        assert_that(english_words_1).is_equal_to(english_words_2)

    def test_english_words_is_dict(self, english_words):
        assert_that(english_words).is_instance_of(dict)

    def test_english_words(self, english_words, english_word_example):
        assert_that(english_words).contains(english_word_example)
