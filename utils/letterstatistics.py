

def update_dict(dic, **kwargs):
    for key in dic:
        if key in kwargs['dict']:
            kwargs['dict'][key] += dic[key]
        else:
            kwargs['dict'][key] = dic[key]


class LetterStatistics:

    def __init__(self, **kwargs):
        self.words = kwargs['dict']
        self.letters = {}
        self.bigrams = {}
        self.total_letters = 0
        self.letters_bigram_ratio = 0.8
        self.__initialize__()

    def __initialize__(self):
        keys = self.words.keys()
        for key in keys:
            self.__letter_count(key)
        self.letters = {k: v / self.total_letters for k, v in self.letters.items()}
        self.bigrams = {k: v / self.total_letters for k, v in self.bigrams.items()}

    def __letter_count(self, word):
        letter_dict = {}
        bigram_dict = {}
        for i in range(len(word)):
            if not word[i].isalpha():
                self.total_letters -= 1
                continue
            if word[i] in letter_dict:
                letter_dict[word[i]] += 1
            else:
                letter_dict[word[i]] = 1
            if i < len(word) - 1:
                if word[i:i + 2] in bigram_dict and word[i:i+2].isalpha():
                    bigram_dict[word[i:i + 2]] += 1
                else:
                    bigram_dict[word[i:i + 2]] = 1
        self.total_letters += len(word)
        update_dict(letter_dict, dict=self.letters)
        update_dict(bigram_dict, dict=self.bigrams)

    def update_dict(self, words):
        self.__init__(dict=words)

    def score(self, word):
        score = 0
        if not word.isalpha():
            return -1
        for i in range(len(word)):
            try:
                score += self.letters[word[i]] * self.letters_bigram_ratio
                if i < len(word) - 1:
                    score += self.bigrams[word[i:i+2]] * (1 - self.letters_bigram_ratio)
            except KeyError:
                return -1
        return score
