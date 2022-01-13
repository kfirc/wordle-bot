import pytest
from assertpy import assert_that


class TestInterface:
    def test_interface_with_simple_input(self, interface):
        interface.post_guess('abcde')
        interface.post_guess('xyzab')
        interface.post_guess('asdfg')
        interface.post_guess('qwert')
        interface.post_guess(interface.answer)

        assert_that(interface.results()).is_true()

    def test_interface_with_one_correct_guess(self, interface):
        interface.post_guess(interface.answer)
        assert_that(interface.results()).is_true()

    def test_interface_with_invalid_input(self, interface, invalid_interface_guess):
        with pytest.raises(ValueError):
            interface.post_guess(invalid_interface_guess)

    def test_interface_with_too_many_guesses(self, interface):
        for _ in range(interface.validator.number_of_tries):
            interface.post_guess('abcde')

        assert_that(interface.results()).is_false()

        for _ in range(5):
            with pytest.raises(ValueError):
                interface.post_guess('abcde')

        assert_that(interface.results()).is_false()

    @pytest.mark.parametrize('answer, guess, result', [
        ('beard', 'aaaaa', 'a?a?a!a?a?'),
        ('beard', 'kiref', 'k/i/r?e?f/'),
        ('zzzzz', 'zabcd', 'z!a/b/c/d/'),
        ('zzzzz', 'zzzzz', 'z!z!z!z!z!'),
    ])
    def test_guess_results(self, interface, answer, guess, result):
        interface.answer = answer
        guess_result = interface.post_guess(guess)
        assert_that(guess_result).is_equal_to(result)
