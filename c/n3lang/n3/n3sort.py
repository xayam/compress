from typing import List

from n3utils import colorize_swap


def n3c_sort(input_data: List[int], verbose=0) -> dict:
    data = input_data[:]
    # print(data)
    width = len(data)
    ones = 0
    for i in data:
        if i == 1:
            ones += 1
    best = [1] * ones + [0] * (width - ones)
    outputs = {
        "data": best,
        "count": 0,
        "ones": ones,
        "zeros": width - ones,
    }
    if best == data:
        return outputs
    count = 0
    count1 = 0
    data = input_data[:]
    pos = width - 1
    flag = False
    while best != data:
        count1 += 1
        for position in range(pos, 0, -1):
            # if data[position - 1] == 0 and data[position] == 1:
            message = f"{colorize_swap(data, position, position - 1)} -> "
            data[position], data[position - 1] = data[position - 1], data[position]
            message += f"{colorize_swap(data, position, position - 1)}"
            if verbose > 0:
                print(message)
            count += 1
            if best == data:
                flag = True
                break
        if flag:
            break
        for position in range(pos, 1, -2):
            # if data[position - 2] == 0 and data[position] == 1:
            message = f"{colorize_swap(data, position, position - 2)} -> "
            data[position], data[position - 2] = data[position - 2], data[position]
            message += f"{colorize_swap(data, position, position - 2)}"
            if verbose > 0:
                print(message)
            count += 1
            if best == data:
                flag = True
                break
        if count1 > 10:
            break
    outputs = {
        "data": best,
        "count": count,
        "ones": ones,
        "zeros": width - ones,
    }
    return outputs


if __name__ == "__main__":
    pass
