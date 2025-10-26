# Task_1
def logger(func):
    def vrapper(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        all_args = args_repr + kwargs_repr
        print(f"{func.__name__} викликана з {', '.join(all_args)}")
        return func
    return vrapper
    @logger
    def add(x, y):
        return x + y
    @logger
    def square_all(*args):
        return [arg ** 2 for arg in args]
# Task_2
from functools import wraps
def stop_words(words: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            return result
        return wrapper
    return decorator
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} п'є pepsi у своєму новенькому BMW!"
assert create_slogan("Steve") == "Steve п'є * у своєму новенькому *!"
print(create_slogan("Steve"))  # Виведе: Steve п'є * у своєму новенькому *!
# Task_3
import functools
def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args:
                arg_to_check = args[0]
            elif kwargs and len(kwargs) == 1:
                arg_to_check = next(iter(kwargs.values()))
            else:
                return func(*args, **kwargs)
            if not isinstance(arg_to_check, type_):
                reason = f"Помилка перевірки: Тип аргументу '{arg_to_check}' ({type(arg_to_check).__name__}) не відповідає очікуваному типу ({type_.__name__})."
                print(reason)
                return False
            if hasattr(arg_to_check) and len(arg_to_check) > max_length:
                reason = f"Помилка перевірки: Довжина аргументу '{arg_to_check}' ({len(arg_to_check)}) перевищує максимальну дозволену довжину ({max_length})."
                print(reason)
                return False
            for item in contains:
                if item not in arg_to_check:
                    reason = f"Помилка перевірки: Аргумент '{arg_to_check}' не містить обов'язковий елемент '{item}'."
                    print(reason)
                    return False
            return func(*args, **kwargs)
            return wrapper
        return decorator
    @arg_rules(type_=str, max_length=15, contains=['05', '@'])
    def create_slogan(name: str) -> str:
        return f"{name} drinks pepsi in his brand new BMW!"
    assert create_slogan('johndoe05@gmail.com') is False
    assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

