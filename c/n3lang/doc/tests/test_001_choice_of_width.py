import math

import winsound

import n3lang.n3sort
from n3utils import progress, colorize_bool

import functools
import matplotlib.pyplot as plt


def difficult():
    try:
        width = int(input("Input maximum width, default 1: "))
    except ValueError:
        width = 1
        print(f"[INFO]| width set to {width} ")
    assert width > 0
    current = 1
    plt.figure(figsize=[4, 2])
    plt.axis([0, 10, 0, 5])
    while current <= width:
        bits_ = []
        max_bits_ = 0
        max_count_ = 0
        max_percent_ = 0
        c = 0
        for limit in range(2 ** current):
            c += 1
            arr = [int(char) for char in f"{limit:{current}b}".replace(" ", "0")]
            # print(arr)
            _, count, ones, zero = n3lang.n3sort.n3c_sort(arr)
            bits = math.ceil(math.log2(ones + 1))
            bits += math.ceil(math.log2(current))
            bits_.append(bits)
            if bits > max_bits_:
                max_bits_ = bits
            if count > max_count_:
                max_count_ = count
            percent_ = 100 * max_bits_ / current
            if percent_ > max_percent_:
                max_percent_ = percent_
            format_percent = str(max_percent_)[0:6]
            if max_percent_ < 100:
                format_percent = " " + format_percent
            if max_percent_ == 0.:
                format_percent = " " + format_percent
            format_percent = format_percent.ljust(7, '0')
            message = f"{str(100 * (limit + 1) / (2 ** current))[0:6].rjust(7, ' ')}% | "
            message += f"width = {str(current).rjust(2, ' ')} | "
            message += f"max_bits_ = {str(max_bits_).rjust(2, ' ')} | "
            message += f"max_count_ = {str(max_count_).rjust(3, ' ')} | "
            message += f"compressing = {format_percent}% | "
            progress(message)
            # plt.scatter(current, max_count_ / current)
            # plt.pause(0.05)
        print("")
        # result = functools.reduce(lambda a, b: a and b, results_)
        current += 1
    winsound.Beep(2500, 5000)
    # plt.show()

def main():
    difficult()


if __name__ == "__main__":
    main()
