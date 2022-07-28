from functools import wraps


def vowel_filter(func):
    vowel_letters = 'AEIOUY'

    @wraps(func)
    def wrapper():
        result = func()
        return [x for x in result if x.upper() in vowel_letters]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
