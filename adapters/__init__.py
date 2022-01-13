import re


class GuessResultToRegexPattern(str):
    def __new__(cls, guess_results: str):
        regex_pattern = '(?=^'
        letter_results = re.findall('..', guess_results)
        success_letters = [''] * len(letter_results)
        almost_letters = [''] * len(letter_results)
        failed_letters = [''] * len(letter_results)

        for index, (letter, results) in enumerate(letter_results):
            if results == '!':
                success_letters[index] = letter
            if results == '?':
                almost_letters[index] = letter
            if results == '/':
                failed_letters[index] = letter

        for index in range(len(letter_results)):
            if success_letters[index]:
                regex_pattern += success_letters[index]

            else:
                prevented_letters = ''.join(failed_letters)
                if almost_letters[index]:
                    prevented_letters += almost_letters[index]
                regex_pattern += f'[^{prevented_letters}]' if prevented_letters else '.'

        regex_pattern += '$)'

        for letter in almost_letters:
            if letter:
                regex_pattern += f'(?=.*{letter}.*)'

        return str.__new__(cls, regex_pattern)
