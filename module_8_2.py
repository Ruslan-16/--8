def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            if isinstance(item, str):
                raise ValueError
            result += float(item)
        except (TypeError, ValueError):
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        if isinstance(numbers, str):
            numbers = list(numbers)
        if not hasattr(numbers, "__iter__"):
            raise TypeError("Некорректный тип данных")
        total, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data
        return total / count if count > 0 else 0
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Некорректные типы внутри строки
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Только 1 и 3 учитываются
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректная коллекция чисел
