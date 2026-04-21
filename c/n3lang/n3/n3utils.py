import math
import re
import sys

import colorama


def progress(message: str) -> None:
    sys.stdout.write("\r" + message)
    sys.stdout.flush()


def colorize_bool(data: bool) -> str:
    message = colorama.Fore.BLACK
    if data:
        message += colorama.Back.GREEN + f"{data} "
    else:
        message += colorama.Back.RED + f"{data}"
    message += colorama.Style.RESET_ALL
    return message


def colorize(data) -> str:
    message = colorama.Fore.BLACK
    message += colorama.Back.RED + f"{data}"
    message += colorama.Style.RESET_ALL
    return message


def colorize_swap(data: list, from_pos: int, to_pos: int) -> str:
    message = ""
    position = 0
    for d in data:
        if position in [from_pos, to_pos]:
            message += colorize(d)
        else:
            message += str(d)
        position += 1
    return message


def fredkin_gate(_a, _b, _c):
    new_b = (_b & ~_a) | (_c & _a)
    new_c = (_c & ~_a) | (_b & _a)
    return _a, new_b, new_c


def sign_of_subtraction_of_two_one_bits(_a, _b):
    control = _b & 1
    _, _, less = fredkin_gate(control, _a, ~_b & 1)
    return 1 - less


def get_annotation() -> str:
    return """
w - width, длина входной последовательности

9 <-> 6 конфлииктующие числа в десятичной записи

'01001' <-> '00110' конфликтующие числа в бинарной записи

'c=2 o=2 p=0 t=1 e=0' с - count,    общее количество сделанных перестановок.
                      o - ones,     количество единиц в последовательности.
                      p - position,      позиция на которой закончилась сортировка.
                      t - tool,     способ (один из двух),
                                    на котором закончилось изменение последовательности.
                      e - exchange, количество смены tool.
"""


def get_n3sort_values(data: str) -> list:
    pattern = r"f=(\d+)\s+c=(\d+)\s+o=(\d+)\s+p=(\d+)\s+t=(\d+)\s+e=(\d+)"
    result = re.findall(pattern, data)
    if result:
        return [int(i) for i in result[0]]
    else:
        return []


def list_to_str(data: list) -> str:
    return "".join(map(str, data))


def get_sum_width(width: int) -> float:
    summa = 0
    for x in range(1, math.ceil(math.log2(width + 1))):
        summa += math.log2(x + 1)
    return summa
