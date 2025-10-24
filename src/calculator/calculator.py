from src.calculator.tokens import get_tokens
from src.utils.errors import ExpressionError
from src.utils.stack import Stack


class Calculator:
    def __init__(self):
        self.operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '%': lambda a, b: a % b,
            '**': lambda a, b: a ** b,
            '//': lambda a, b: a // b
        }

        self.unary_operators = {
            '~': lambda a: -a,
            '$': lambda a: a,
        }

    def solve(self, expr: str) -> float:
        """
        Добавляет в стек числа при встрече знака делает расчёт
        :param expr: выражение
        :return: результат или ошибку (через raise)
        """
        tokens = get_tokens(expr)
        numbers = Stack()

        try:
            for token, value in tokens:
                if token == "NUM":
                    numbers.push(value)
                elif token in self.unary_operators:
                    numbers.push(self.unary_operators[token](numbers.pop()))
                elif token in self.operators:
                        b = numbers.pop()
                        a = numbers.pop()
                        numbers.push(self.operators[token](a, b))
        except IndexError:
            raise ExpressionError("Операторов больше чем чисел")

        if len(numbers) == 1:
            return numbers.pop()
        else:
            raise ExpressionError("Чисел больше чем операторов")
