import pytest


@pytest.mark.parametrize("number, result", [
    (1, "1"),
    (2, "2"),
    (3, "fizz"),
    (4, "4"),
    (5, "buzz"),
    (9, "fizz"),
    (15, "fizzbuzz"),
    (20, "buzz"),
    (45, "fizzbuzz")
])
def test_fizzbuzz_game(number, result):
    assert result == FizzBuzzGame().Speak(number)


class FizzBuzzGame():
    def Speak(self, number):
        if(self.IsFizz(number) and self.IsBuzz(number)):
            return "fizzbuzz"

        if (self.IsFizz(number)):
            return "fizz"

        if (self.IsBuzz(number)):
            return "buzz"

        return str(number)

    def IsFizz(self, number): return number % 3 == 0

    def IsBuzz(self, number): return number % 5 == 0
