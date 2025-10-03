import math
import re


def circle_square(radius):
    return math.pi * radius**2


print(circle_square(5))


# ======================
# v1
def _zip(list1, list2):
    """
    "Сшивает" два списка в список кортежей.
    Итерация продолжается до конца самого короткого списка.
    """
    _zip = []

    if len(list1) <= len(list2):
        for idx, _ in enumerate(list1):
            _zip.append((list1[idx], list2[idx]))

    if len(list2) < len(list1):
        for idx, _ in enumerate(list2):
            _zip.append((list2[idx], list1[idx]))

    return _zip


# v2
def _zip2(list1, list2):
    """
    "Сшивает" два списка в список кортежей.
    Итерация продолжается до конца самого короткого списка.
    """
    _zip = []
    iteration_count = min(len(list1), len(list2))

    for idx in range(iteration_count):
        _zip.append((list1[idx], list2[idx]))

    return _zip


# --- Пример для проверки вашего решения ---
list_a = [1, 5, 3, 8, 35]
list_b = [2, 7, 9]

# Ожидаемый результат: [(1, 2), (5, 7), (3, 9)]
print(_zip(list_a, list_b))
print(_zip2(list_b, list_a))


# ======================
def final_balance(init_sum, interest_rate, years, round_num=2):
    """
    Рассчитывает итоговую сумму на банковском счете
    с учетом сложного процента и округления.
    """
    return round(init_sum * (1 + interest_rate / 100) ** years, round_num)


# --- Здесь вы можете вызвать вашу функцию для проверки ---

# Пример вызова для первой группы параметров
result1 = final_balance(1000, 5, 10)
print(f"Результат для 1000, 5%, 10 лет: {result1}")

# Пример вызова для второй группы параметров
result2 = final_balance(700, 7, 10)
print(f"Результат для 700, 7%, 10 лет: {result2}")

# Можете также проверить работу округления
# Например, округление до целых (0 знаков)
result3 = final_balance(1000, 5, 10, round_num=0)
print(f"Результат с округлением до целых: {result3}")

# Округление до десятков (-1)
result4 = final_balance(1000, 5, 10, round_num=-1)
print(f"Результат с округлением до десятков: {result4}")

# =================
#


def debbug_array(arr_source, arr_target, active_step):
    print(f"source array | after {active_step} step | ", arr_source)
    print(f"target array | after {active_step} step | ", arr_target)
    print("#############")


def math_task(data):
    answer = []
    # этап 1: возводим в третью степень
    for elem in data:
        answer += [elem**3]

    debbug_array(data, answer, 1)

    # этап 2: берем остаток от деления на 7
    for i in range(len(answer)):
        answer[i] = answer[i] % 7

    debbug_array(data, answer, 2)

    # этап 3: прибавляем к остатку изначальный массив
    for i in range(len(answer)):
        answer[i] = answer[i] + data[i]

    debbug_array(data, answer, 3)

    # возвращаем результат
    return answer


# --- Вызов функции ---
test_data = [1, 2, 3, 4]
final_result = math_task(test_data)
print("\nИтоговый результат:")
print(final_result)

# ==================
#


def sum_as_ints(list_of_string):
    accum = 0
    for el in list_of_string:
        try:
            accum += int(el)
        except ValueError:
            continue
    return accum


data = ["5", "0", "hello", "25", "3.14", "-10"]

# Ожидаемый результат: 5 + 0 + 25 - 10 = 20
print(f"Исходный список: {data}")
print(f"Сумма целых чисел: {sum_as_ints(data)}")

# --- Еще один пример ---
data2 = ["world", "1", "2", "3"]
# Ожидаемый результат: 1 + 2 + 3 = 6
print(f"\nИсходный список: {data2}")
print(f"Сумма целых чисел: {sum_as_ints(data2)}")


# ============
#


def reversed_(array):
    rv = []
    copy = array.copy()
    while copy:
        rv.append(copy.pop())
    return rv


def reversed2(array):
    rv = []
    for idx in range(len(array)):
        rv.append(array[-1 + -idx])

    return rv


def reversed_etalon(array):
    return array[::-1]


if reversed_(reversed_([1, 2, 3])) == [1, 2, 3]:
    print("Вариант 1: Все хорошо")
else:
    raise RuntimeError("Вариант 1: Ошибка!")

print("##############################################")
if reversed2(reversed2([1, 2, 3])) == [1, 2, 3]:
    print("Вариант 1: Все хорошо")
else:
    raise RuntimeError("Вариант 1: Ошибка!")

result_1 = reversed_([1, 2, 3, 4])
result_2 = reversed2([1, 2, 3, 4])
result_3 = reversed_etalon([1, 2, 3, 4])
print(result_1, result_2, result_3)


# ======================
#


def find_substr(sub_str, source_str):
    start_pos = source_str.find(sub_str)
    print(f"SAB:{sub_str}, SOURCE: {source_str}, START: {start_pos}")
    if start_pos == -1:
        return (-1, -1)
    return (start_pos, start_pos + len(sub_str))


# --- Примеры для проверки ---
result1 = find_substr("мы", "Летом мы хотим отдыхать на море")
print(f"Результат 1: {result1}")  # Ожидаемый вывод: (6, 8)

result2 = find_substr("ма", "маленькая машина")
print(f"Результат 2: {result2}")  # Ожидаемый вывод: (0, 2)

result3 = find_substr("кот", "собака и кошка")
print(f"Результат 3 (не найдено): {result3}")  # Ожидаемый вывод: None или (-1, -1)

# ==================
#


def fifth_element(list: list) -> list:
    return list[-5::-5]


# --- Задание для самопроверки (расшифруйте код) ---
encoded_list = [
    "e",
    6,
    8,
    "A",
    ">",
    "^",
    "S",
    "$",
    "R",
    "C",
    6,
    "+",
    "#",
    9,
    "/",
    1,
    "T",
    "!",
    "%",
    "K",
    7,
    "-",
    "O",
    "*",
    "<",
    2,
    "h",
    4,
    "g",
]

# Примените вашу функцию к этому списку
decoded_list = fifth_element(encoded_list)
print(f"Зашифрованный список: {encoded_list}")
print(f"Расшифрованный результат: {decoded_list}")


def process_string(string: str) -> str:
    return string[1:].lower().replace("intern", "junior")


input_string = "IIntern reads a lot of books about Interns"
processed_string = process_string(input_string)
print(f"Исходная строка: '{input_string}'")
print(f"Обработанная строка: '{processed_string}'")

# =========================
#


def check_string(text):
    if text != text.strip():
        return False

    if not text[-1:] == ".":
        return False

    for idx, el in enumerate(text.strip().split()):
        if (idx == 0 and not el.istitle()) or (idx > 0 and el.istitle()):
            return False

    return True


# Тестовые данные для проверки
string1 = "В этом году будет особенно теплое море."  # Ожидаем True
string2 = "В этом году будет особенно теплое Mоре."  # Ожидаем False (второе слово с большой буквы)
string3 = "В этом году будет особенно теплое море"  # Ожидаем False (нет точки в конце)
string4 = " В этом году будет особенно теплое море."  # Ожидаем False (пробел в начале)
string5 = "в этом году будет особенно теплое море."  # Ожидаем False (первое слово с маленькой буквы)

# Можешь вызвать функцию для каждой строки и посмотреть, что она вернет
print(f"'{string1}': {check_string(string1)}")
print(f"'{string2}': {check_string(string2)}")
print(f"'{string3}': {check_string(string3)}")
print(f"'{string4}': {check_string(string4)}")
print(f"'{string5}': {check_string(string5)}")
