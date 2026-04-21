from n3compress import n3c_sort, n3c_recovery
from n3utils import colorize_bool, progress


def main(w, verbose=1):
    if verbose >= 2:
        print(f"Current WIDTH = {w}")
    count = 0
    result_ = True
    percent_ = 0.
    bits_ = 0
    max_count_ = 0
    max_one_ = 0
    for z in range(2 ** w):
        count += 1
        arr = [int(char) for char in f"{z:{w}b}".replace(" ", "0")]
        # arr = [random.choice([0, 1]) for _ in range(w)]
        printable = False
        if verbose >= 3:
            printable = True
        result, percent, bits, max_count, max_one = n3c_sort(arr, printable)
        result_ = result_ and result
        result = colorize_bool(result_)
        percent = float(percent.replace(' ', ''))
        if percent > percent_:
            percent_ = percent
        if bits > bits_:
            bits_ = bits
        if max_count > max_count_:
            max_count_ = max_count
        if max_one > max_one_:
            max_one_ = max_one
        printable = False
        if verbose >= 2:
            printable = True
        data = n3c_recovery(
            _width=w,
            _count=max_count,
            _one=max_one,
            printable=printable
        )
        if verbose >= 2:
            print(f"original_data={arr}")
            print(f"decompress_data={data}")
        if not data:
            raise Exception("[ERROR] | Data not found")
        if data == arr:
            warning = colorize_bool(True)
        else:
            raise Exception("[ERROR] | input_data != decompress_data")
        message = \
            f"{str(percent_)[0:6].rjust(6, ' ')}, " + \
            f"{warning}, {result}, {count}/{2 ** w}, " + \
            f"bits_={bits_}, w={w}, max_count_={max_count_}, max_one_={max_one_}"
        if verbose == 1:
            progress(message)
        elif verbose >= 2:
            print(message)
    if verbose == 1:
        print("")


if __name__ == "__main__":
    # you may set range from 0 and more
    # error when width=4
    for width in range(1, 4):
        # for disable output set param 'verbose' to 0
        # for get minimum information set param 'verbose' to 1
        # for get more information set param 'verbose' to 2 or 3
        main(width, verbose=1)
