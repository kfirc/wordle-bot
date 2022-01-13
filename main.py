from utils.words import EnglishWords
from utils.letterstatistics import LetterStatistics

if __name__ == '__main__':
    english_words = EnglishWords()
    letters = LetterStatistics(dict=english_words)
    print(letters.score("anger"))
    print(letters.score("outer"))
    print(letters.score("extra"))
    print(letters.score("small"))


