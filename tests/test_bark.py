import pytest

from src.calculator.calculator import Calculator
from src.utils.errors import InputError, ParenthesisError, ExpressionError

calc = Calculator()


@pytest.mark.parametrize(
    "expr, error",
    [
        ("meow", InputError),
        ("4 meow +", InputError),
        ("   ", InputError),
        ("", InputError),

        ("(", ParenthesisError),
        (")*  ", ParenthesisError),

        ("3 2 * *  ", ExpressionError),
        ("3 2 4 5 * *", ExpressionError),

        ("3 2 4 5 * * 0 /", ZeroDivisionError),
        ("3 2 4 5 * * 2.1 * 0 //", ZeroDivisionError),
        ("1 2* 0%", ZeroDivisionError),

        ("3.14 1000 ** ", OverflowError),
    ])
def test(expr: str, error):
    with pytest.raises(error):
        calc.solve(expr)
