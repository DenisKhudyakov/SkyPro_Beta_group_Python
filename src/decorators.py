import datetime
import functools
from typing import Callable, Any


def log(*, filename: str = "") -> Callable:
    """
    Декоратор, который логирует вызов функций.
    :param filename: файл куда записывать логи, по умолчанию его нет.
    :return: Возвращаем задекорированную функцию
    """

    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args, **kwargs):
            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as file:
                        file.write(f"{date_time} {func.__name__} ok\n")
                else:
                    print(f"{date_time} {func.__name__}\n")
            except Exception as ex:
                if filename:
                    with open(filename, "a") as f:
                        f.write(
                            "{} {} error: <{}>. Inputs: ({}, {})\n".format(
                                date_time, func.__name__, str(ex), args, kwargs
                            )
                        )
                else:
                    print(
                        "{} {} error: <{}>. Inputs: ({}, {})\n".format(date_time, func.__name__, str(ex), args, kwargs)
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
