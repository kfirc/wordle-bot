from functools import lru_cache
from typing import List

import constants


class WordleGuessValidator:
    def __init__(self, number_of_letters, number_of_tries):
        self.number_of_letters = number_of_letters
        self.number_of_tries = number_of_tries

    def validate(self, guess: str):
        if self.number_of_tries <= 0:
            raise ValueError('No more guesses!')

        if not isinstance(guess, str):
            raise ValueError('Guess must be a string')

        if len(guess) != self.number_of_letters:
            raise ValueError(f'Guess must contain exactly {self.number_of_letters} letters')

        if not guess.isalpha():
            raise ValueError('Guess must be alphabetical')

        return guess.lower()


class WordleGuess:
    def __init__(self, guess, answer, validator):
        self.answer = answer
        self.validator = validator
        self.guess = self.validator.validate(guess)

    @lru_cache
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


class WordleInterface:
    def __init__(self):
        self.answer = 'beard'
        self.validator = WordleGuessValidator(
            number_of_letters=len(self.answer),
            number_of_tries=constants.NUMBER_OF_TRIES,
        )
        self.guesses: List[WordleGuess] = []
        self.guesses_results: List[str] = []

    def post_guess(self, guess: str):
        wordle_guess = WordleGuess(guess, self.answer, self.validator)
        self.guesses.append(wordle_guess)
        self.guesses_results.append(wordle_guess.results())
        self.validator.number_of_tries -= 1

        return wordle_guess.results()

    def results(self):
        is_winner = self.guesses[-1].guess == self.answer

        if not is_winner and self.validator.number_of_tries:
            return None

        return is_winner

    def __repr__(self):
        return '\n'.join(self.guesses_results)
