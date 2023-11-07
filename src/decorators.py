import datetime
import functools
from typing import Callable, Any


def log(*, filename: str = "") -> Callable:
    """
    Декоратор, который логирует вызов функций.
    :param file_name: файл куда записывать логи, по умолчанию его нет.
    :return: Возвращаем задекорированную функцию
    """

    def wrapper(funk: Callable) -> Callable:
        @functools.wraps(funk)
        def inner(*args, **kwargs):
            date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                funk(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{date_time} {funk.__name__} ok\n")
                else:
                    print(f"{date_time}{funk.__name__}\n")
            except Exception as ex:
                if filename:
                    with open(filename, "a") as f:
                        f.write(
                            "{} {} error: <{}>. Inputs: ({}, {})\n".format(
                                date_time, funk.__name__, str(ex), *args
                            )
                        )
                else:
                    print(
                        "{} {} error: <{}>. Inputs: ({}, {})\n".format(
                            date_time, funk.__name__, str(ex), *args
                        )
                    )

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


@log(filename="mylog.txt")
def my_function1(x, y):
    return x + y / 0


@log()
def my_function2(x, y):
    return x + y


if __name__ == "__main__":
    my_function(1, 2)
    my_function1(1, 2)
    my_function2(1, 2)
