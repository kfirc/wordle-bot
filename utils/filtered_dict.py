import re
import copy


class FilteredDict(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.words_dict = copy.copy(self)

    def filter(self, regex_pattern):
        regex_ob = re.compile(regex_pattern)
        for item in self.words_dict.items():
            filtered_word = regex_ob.fullmatch(item[0])
            if not filtered_word:  # is not None
                self.pop(item[0])

    def reset(self):
        self.update(self.words_dict)
