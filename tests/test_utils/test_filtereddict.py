from assertpy import assert_that as ass_that
from utils.filtered_dict import FilteredDict


class TestFilteredDict:

    def test_filtered_dict_is_dictionary(self, english_words):
        fd = FilteredDict(english_words)
        ass_that(fd).is_instance_of(dict)

    def test_filtered_dict_remove_all_words(self, english_words):
        fd = FilteredDict(english_words)
        new_fd = FilteredDict(english_words)
        regex = ""
        fd.filter(regex)
        ass_that(fd).is_equal_to(new_fd)

    def test_filtered_dict_no_filter(self, english_words):
        fd = FilteredDict(english_words)
        regex = ".*"
        fd.filter(regex)
        ass_that(fd).is_equal_to(english_words)

    def test_filtered_dict_filter_one_word(self, english_words, english_word_second_example):
        fd = FilteredDict(english_words)
        fd.filter(english_word_second_example)
        if english_word_second_example in english_words.keys():
            ass_that(fd).is_equal_to({english_word_second_example: 1})
        else:
            ass_that(fd).is_equal_to({})

    def test_filtered_dict_filter_specific_length_letters_words(self, english_words, length):
        fd = FilteredDict(english_words)
        regex = "." * length
        fd.filter(regex)
        test_dict = {}
        for item in english_words.items():
            if len(item[0]) == length:
                test_dict[item[0]] = item[1]
        ass_that(fd).is_equal_to(test_dict)