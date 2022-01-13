
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
        self.positions = {}
        self.total_letters = 0
        self.letters_ratio = 0.3
        self.position_ratio = 0.5
        self.bigram_ratio = 0.2
        self.__initialize__()

    def __initialize__(self):
        keys = self.words.keys()
        for key in keys:
            self.__letter_count(key)
        self.letters = {k: v / self.total_letters for k, v in self.letters.items()}
        self.bigrams = {k: v / self.total_letters for k, v in self.bigrams.items()}
        for pos in self.positions.keys():
            total_letters = self.positions[pos]['total']
            self.positions[pos].pop('total')
            self.positions[pos] = {k: v / total_letters for k, v in self.positions[pos].items()}

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
            self.__update_positions(i, word[i])
        self.total_letters += len(word)
        update_dict(letter_dict, dict=self.letters)
        update_dict(bigram_dict, dict=self.bigrams)

    def update_dict(self, words):
        self.__init__(dict=words)

    def __update_positions(self, index, letter):
        if index not in self.positions:
            self.positions[index] = {'total': 0, letter: 1}
        elif letter not in self.positions[index]:
            self.positions[index][letter] = 1
        else:
            self.positions[index][letter] += 1
        self.positions[index]['total'] += 1

    def score(self, word):
        score = 0
        if not word.isalpha():
            return -1
        for i in range(len(word)):
            try:
                score += self.letters[word[i]] * self.letters_ratio
                score += self.positions[i][word[i]] * self.position_ratio
                if i < len(word) - 1:
                    score += self.bigrams[word[i:i+2]] * self.bigram_ratio
            except KeyError:
                return -1
        return score