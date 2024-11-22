
def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return a + b
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return f"{a}{b}"
        elif isinstance(a, str) and isinstance(b, (int, float)):
            return f"{a}{b}"
        else:
            raise TypeError("Ошибка.")
    except TypeError as e:
        print(f"Внимание! : {e}")
        raise

# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up([1, 2, 3], "строка"))

