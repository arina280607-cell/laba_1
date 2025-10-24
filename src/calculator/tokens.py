import re

from src.utils.errors import ParenthesisError, InputError
from src.utils.stack import Stack

Token = tuple[str, float | None]  # ("NUM", 12.5) или ("+", None) и т.д.


def get_tokens(expr: str) -> list[Token]:
    """
    Возвращает токены из исходного выражения
    :param expr: выражение
    :return: список токенов

    """

    regex = re.compile(r"""
    \s*
    (
        \d+(?:\.\d+)?         # число
      | \*\*                  # ** (раньше *)
      | //                    # //
      | [%()+\-~$*/]          # одиночные токены
    )
""", re.VERBOSE)
    expr = expr.strip()
    if not expr:
        raise InputError("Пустой ввод")  # Провека, является ли входная строка пустой или состоящей только из пробелов

    pos = 0
    output: list[Token] = []
    parenthesis = Stack()
    while pos < len(expr):
        m = regex.match(expr, pos)
        if not m:
            raise InputError(f"Некорректный ввод около: '{expr[pos:]}'")
        element = m.group(1)
        pos = m.end()

        if element[0].isdigit():
            output.append(("NUM", float(element)))
        else:
            if element == "(":
                parenthesis.push(element)
            elif element == ")":
                if parenthesis.is_empty():
                    raise ParenthesisError(
                        "Ошибка ввода. Несбалансированные скобки: закрывающая скобка без открывающей")
                parenthesis.pop()
            else:
                output.append((element, None))
    if not parenthesis.is_empty():
        print(parenthesis)
        raise ParenthesisError("Несбалансированные скобки: есть незакрытые скобки")

    output.append(('EOF', None))
    return output
