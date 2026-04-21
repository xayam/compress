import math

from n3utils import colorize_swap, get_sum_width, list_to_str


def n3c_recovery(width: int,
                 count: int,
                 ones: int,
                 last: int,
                 verbose: int=0) -> str:
    best = [1] * ones + [0] * (width - ones)
    # limit = 2 ** math.ceil(get_sum_width(width - 1))
    pos = 0
    data = best[:]
    flag = False
    while count > 0:
        print(last, data)
        if last == 2:
            for position in range(pos, width - 2):
                if data[position + 2] == 0 and data[position] == 1:
                    message = f"{colorize_swap(data, position, position + 2)} -> "
                    data[position], data[position + 2] = data[position + 2], data[position]
                    message += f"{colorize_swap(data, position, position + 2)}"
                    if verbose > 0:
                        print(message)
                    count -= 1
                    # if count == 0:
                    break
            last = 1
        elif last == 1:
            for position in range(pos, width - 1):
                if data[position + 1] == 0 and data[position] == 1:
                    message = f"{colorize_swap(data, position, position + 1)} -> "
                    data[position], data[position + 1] = data[position + 1], data[position]
                    message += f"{colorize_swap(data, position, position + 1)}"
                    if verbose > 0:
                        print(message)
                    count -= 1
                    # if count == 0:
                    break
            last = 2
    return list_to_str(data)

# if position == width - 1:
#     position = 0
# elif degrees[position] == 1:
#     if position == width - 1:
#         tool = 0
#         tool_change -= 1
#     elif degrees[position + 2] == 1:
#         if degrees[position + 1] == 1:
#             position += 2
#         else:
#             pass
#     else:
#         message = f"{colorize_swap(degrees, position, position + 2)} -> "
#         degrees[position], degrees[position + 2] = degrees[position + 2], degrees[position]
#         message += f"{colorize_swap(degrees, position, position + 2)}"
#         if verbose > 0:
#             print(message)
#         count -= 1
#         position += 2
# else:
#     position += 1
