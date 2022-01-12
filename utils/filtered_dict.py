import re


class FilteredDict(dict):

    def __init__(self, dic, **kwargs):
        super().__init__(**kwargs)
        self.words_dict = dic
        self.__first_filter = True

    def filter(self, regex_pattern):
        regex_ob = re.compile(regex_pattern)
        temp_dict = self
        if self.__first_filter:  # if it's the first run -
            temp_dict = self.words_dict
            self.__first_filter = False
        for item in temp_dict.items():
            filtered_word = regex_ob.fullmatch(item[0])
            if filtered_word:  # is not None
                self[item[0]] = item[1]

    def reset(self):
        self.clear()
        self.__first_filter = True
