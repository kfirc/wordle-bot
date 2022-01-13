import random
import logging
from abc import ABC, abstractmethod

from adapters import GuessResultToRegexPattern
from utils.filtered_dict import FilteredDict
from utils.words import EnglishWords
from wordle_interface import WordleInterfaceAbstract

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


class WordleBotAbstract(ABC):
    logger = logger

    @abstractmethod
    def __init__(self, interface: WordleInterfaceAbstract):
        self.interface = interface

    @abstractmethod
    def generate_guess(self) -> str:
        return 'guess'

    @abstractmethod
    def post_guess_result(self, guess_result: str):
        pass

    @abstractmethod
    def reset(self):
        pass

    def start(self):
        print('Game starts!')

        while self.interface.results() is None:
            print(f'\nRemaining guesses: {self.interface.validator.number_of_tries}')
            guess = self.generate_guess()
            guess_result = self.interface.post_guess(guess)
            self.post_guess_result(guess_result)

        print(f'Game results: {self.interface.results()}.')
        self.reset()


class WordleBot(WordleBotAbstract):
    def __init__(self, interface):
        self.interface = interface

        self.words = EnglishWords()
        self.words = FilteredDict(self.words)
        self.words = self.words.filter('^.{5}$')
        self.words = FilteredDict(self.words)

    def generate_guess(self) -> str:
        guess = random.choice(list(self.words.keys()))
        print(f'Generated guess: {guess}')
        return guess

    def post_guess_result(self, guess_result: str):
        print(f'Guess result: {guess_result}')
        regex_pattern = GuessResultToRegexPattern(guess_result)
        self.words.filter(regex_pattern)
        print(f'Remaining words: {len(self.words)}')

    def reset(self):
        self.words.reset()
        print('Bot is reset.')
