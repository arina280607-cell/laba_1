class CalcError(Exception):
    """Понятные ошибки калькулятора."""
    pass


class ParenthesisError(CalcError):
    """Ошибка, связанная со скобками"""
    pass
