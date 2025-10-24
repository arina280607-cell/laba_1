from src.calculator.calculator import Calculator
from src.utils.errors import CalcError


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    print("Калькулятор.\nВведите выражение в обратной польской нотации.\nДля завершения работы введите 'конец'")

    while True:
        try:
            i = input()
            calc = Calculator()
            if i.lower() == "конец":
                break
            result = calc.solve(i)
            if result.is_integer():
                result = int(result)
            print(result)
        except CalcError as e:
            print(e)
        except ZeroDivisionError:
            print("Делить на ноль нельзя!")
        except OverflowError:
            print("Слишком большое выражение. Попробуйте ввести что-то попроще")


if __name__ == "__main__":
    main()
