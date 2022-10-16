"""
Oleg's code

Селянта Олег Дмитриевич

P3114

"""


import math

def print_table(code, right_code, error_ind):
    print('Исходный код:     ' + ' '.join(code))
    if error_ind:
        print('Ошибочный разряд: ' + ' ' * 2 * (error_ind - 1) + '^')
    else:
        print('Ошибок при передаче не обнаружено.')
    print()
    print('Исходные данные:  ' + get_data(right_code))


def get_data(right_code):
    # Получение строки с данными из исправленного кода Хэмминга
    data = list()
    for i in range(1, len(right_code) + 1):
        if math.log2(i) % 1 != 0:
            data.append(right_code[i - 1])
    return ''.join(data)


def get_right_code(code, err_ind):
    # Исправление кода Хэмминга с известным индексом ошибки
    return code[:err_ind - 1] + (
        '0' if code[err_ind - 1] == '1' else '1') + code[err_ind:]


def count_need_r(code):
    # Подсчет минимального количества проверочных разрядов
    for i in range(1000):
        if i >= math.log2(len(code) + 1):
            return i


def count_s(code, ind):
    # Подсчет синдрома для определенного разряда
    def get_list_s(code, ind):
        # Получение массива с данными для вычисления синдрома
        res = list()
        for i in range(2 ** ind - 1, len(code), 2 * 2 ** ind):
            for j in range(2 ** ind):
                try:
                    res.append(code[i + j])
                except IndexError:
                    break
        return res

    list_s = get_list_s(code, ind)
    return sum(map(int, list_s)) % 2


code = input('Введите код Хэмминга: ')  # Считывание кода
# Проверка на ошибки
if set(code) - {'0', '1'} != set():  # Проверка вводимых символов (чтобы были только 0 или 1)
    print('>>> Код состоит не из символов 0 и 1.')
    exit()
if len(code) == 0:
    print('>>> Введена пустая строка.')
    exit()


need_r = count_need_r(code)  # Подсчёт требуемого числа проверочных разрядов
s = [count_s(code, i) for i in range(need_r)]  # Последовательность синдромов
error = sum([2 ** i * s[i] for i in range(need_r)])  # Номер разряда с ошибкой
if error > len(code):
    print('>>> Ошибка более чем в 1 бите.')
    exit()
right_code = get_right_code(code, error) if error else code  # Исправленный код
print_table(code, right_code, error)  # Печать результатов программы