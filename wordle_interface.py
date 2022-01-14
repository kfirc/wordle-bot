import random
from abc import ABC, abstractmethod
from functools import lru_cache
from typing import List

import constants
from utils.filtered_dict import FilteredDict
from utils.words import EnglishWords


class WordleGuessValidator:
    def __init__(self, number_of_letters, number_of_tries):
        self.number_of_letters = number_of_letters
        self.number_of_tries = number_of_tries

    def validate(self, guess: str):
        if self.number_of_tries <= 0:
            raise ValueError(f'No more guesses! guess={guess}')

        if not isinstance(guess, str):
            raise ValueError(f'Guess must be a string. guess={guess}')

        if len(guess) != self.number_of_letters:
            raise ValueError(f'Guess must contain exactly {self.number_of_letters} letters. guess={guess}')

        if not guess.isalpha():
            raise ValueError(f'Guess must be alphabetical. guess={guess}')


class WordleGuess:
    def __init__(self, guess: str, answer: str):
        self.answer = answer
        self.guess = guess.lower()

    @property
    def is_true(self):
        return self.guess == self.answer

    @lru_cache()
    def results(self):
        results = ''

        for index in range(len(self.guess)):
            if self.guess[index] == self.answer[index]:
                results += f'{self.guess[index]}!'

            elif self.guess[index] in self.answer:
                results += f'{self.guess[index]}?'

            else:
                results += f'{self.guess[index]}/'

        return results

    def __repr__(self):
        return f'{self.guess} - {self.is_true}'


class WordleInterfaceAbstract(ABC):
    @abstractmethod
    def post_guess(self, guess: str) -> str:
        return 'g/u?e!s/s?'

    @abstractmethod
    def results(self) -> bool:
        return True


class WordleInterface(WordleInterfaceAbstract):
    def __init__(self):
        self.answer = self._generate_answer()
        self.validator = WordleGuessValidator(
            number_of_letters=len(self.answer),
            number_of_tries=constants.NUMBER_OF_TRIES,
        )
        self.guesses: List[WordleGuess] = []
        self.guesses_results: List[str] = []

    @staticmethod
    def _generate_answer():
        words = FilteredDict(EnglishWords()).filter(f'^.{{{constants.NUMBER_OF_LETTERS}}}$')
        return random.choice(list(words.keys()))

    def post_guess(self, guess: str):
        self.validator.validate(guess)
        self.validator.number_of_tries -= 1

        wordle_guess = WordleGuess(guess, self.answer)
        self.guesses.append(wordle_guess)
        self.guesses_results.append(wordle_guess.results())

        return wordle_guess.results()

    def results(self):
        if not self.guesses or (self.validator.number_of_tries and not self.guesses[-1].is_true):
            return None

        return self.guesses[-1].is_true

    def __repr__(self):
        return '\n'.join(self.guesses_results)
