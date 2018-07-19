import pytest


@pytest.mark.parametrize("number, result", [
    (1, "1"),
    (2, "2"),
    (3, "fizz"),
    (4, "4"),
    (5, "buzz"),
    (7, "pop"),
    (9, "fizz"),
    (15, "fizzbuzz"),
    (20, "buzz"),
    (21, "fizzpop"),
    (28, "pop"),
    (35, "buzzpop"),
    (45, "fizzbuzz"),
    (63, "fizzpop"),
    (70, "buzzpop"),
    (105, "fizzbuzzpop")
])
def test_fizzbuzz_game(number, result):
    assert result == FizzBuzzGame().Speak(number)


class FizzBuzzGame():
    def __init__(self):
        self._lookup = {3: "fizz", 5: "buzz", 7: "pop"}

    def Speak(self, number):
        result = ""

        for key in self._lookup:
            if(number % key == 0):
                result = result + self._lookup[key]

        if (result != ""):
            return result

        return str(number)
