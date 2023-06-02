# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime
import time

WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
                       '__annotations__')
WRAPPER_UPDATES = ('__dict__',)


def update_wrapper(wrapper,
                   wrapped,
                   assigned=WRAPPER_ASSIGNMENTS,
                   updated=WRAPPER_UPDATES):
    for attr in assigned:
        try:
            value = getattr(wrapped, attr)
        except AttributeError:
            pass
        else:
            setattr(wrapper, attr, value)
    for attr in updated:
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))
    wrapper.__wrapped__ = wrapped
    return wrapper


def custom_wraps(wrapped,
                 assigned=WRAPPER_ASSIGNMENTS,
                 updated=WRAPPER_UPDATES):
    return partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)


class partial:
    __slots__ = "func", "args", "keywords", "__dict__", "__weakref__"

    def __new__(cls, func, /, *args, **keywords):
        if hasattr(func, "func"):
            args = func.args + args
            keywords = {**func.keywords, **keywords}
            func = func.func

        self = super(partial, cls).__new__(cls)

        self.func = func
        self.args = args
        self.keywords = keywords
        return self

    def __call__(self, /, *args, **keywords):
        keywords = {**self.keywords, **keywords}
        return self.func(*self.args, *args, **keywords)


# Здесь пишем код
def func_log(file_log='log.txt'):
    def decorator(func):
        @custom_wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_log, 'a', encoding='utf-8') as file:
                timestamp = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
                log_text = f"{func.__name__} вызвана {timestamp}\n"
                file.write(log_text)
            return func(*args, **kwargs)

        # wrapper.__module__ = getattr(func, '__module__')
        # wrapper.__doc__ = getattr(func, '__doc__')
        # wrapper.__name__ = getattr(func, '__name__')
        # wrapper.__qualname__ = getattr(func, '__qualname__')
        # wrapper.__annotations__ = getattr(func, '__annotations__', {})
        return wrapper

    return decorator


@func_log()
def func1(a=1):
    """Some function description"""
    print(a)
    time.sleep(3)


@func_log(file_log='func2.txt')
def func2():
    time.sleep(5)


help(func1)

# func1()
# func2()
# func1()
