class CalcError(Exception):
    """Понятные ошибки калькулятора."""
    pass

class InputError(Exception):
    """Неверный ввод"""
    pass
class ParenthesisError(CalcError):
    """Ошибка, связанная со скобками"""
    pass

class ExpressionError(CalcError):
    """
    Ошибка, связанная с несогласованием элементов

    Примеры:
     - 3 2 * * -> Операторов больше чем чисел
     - 3 2 4 5 * * -> Чисел больше чем операторов
    """
    pass