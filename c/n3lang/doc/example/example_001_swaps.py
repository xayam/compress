import winsound

from n3compress import n3c_sort


def main(_data: str, verbose=1) -> [list, list]:
    w = len(_data)
    if verbose > 0:
        print(f"Current width = {w}")
    arr = [int(char) for char in _data]
    result, percent, bits, max_count, max_one = \
        n3c_sort(
            arr,
            printable=False,
            verbose=verbose
        )
    if verbose > 0:
        print(
            f"result={result}, percent={percent}, " +
            f"bits={bits}, max_count={max_count}, max_one={max_one}"
        )
    r = []
    # r = n3c_recovery(
    #         _width=w,
    #         _count=max_count,
    #         _one=max_one,
    #         printable=False,
    #         verbose=verbose
    # )
    # return arr, r
    return max_count, max_one


def test1():
    width = 0
    while True:
        width += 1
        pars = []
        for data in range(2 ** width):
            arr = f"{data:{width}b}".replace(" ", "0")
            count, one = main(arr, verbose=0)
            pars.append(f"{count}_{one}")
        conflict = 0
        pars.sort()
        for i in range(1, len(pars)):
            if pars[i - 1] == pars[i]:
                conflict += 1
        print(f"width={width} | conflict={conflict} | unique={len(set(pars))}")


def test2():
    width = 0
    valid = False
    while not valid:
        width += 1
        pars = []
        for data in range(2 ** width):
            arr = f"{data:{width}b}".replace(" ", "0")
            count, one = main(arr, verbose=0)
            pars.append(f"{count}_{one}")
            # res = o == i
            # if not res:
            #     i, o = n3c_get_path_by_name(arr, verbose=1)
            # print("Result: " + colorize_bool(res))
            # print(f"Input data1 for compress: {i}")
            # print(f"Output n3c_recovery data1: {o}")
            # print("")
            # input("[ENTER]:")
        conflict = 0
        pars.sort()
        for i in range(1, len(pars)):
            if pars[i - 1] == pars[i]:
                conflict += 1
        print(f"width={width} | 2 ** width={2 ** width} " +
              f"| conflict={conflict} | {conflict / 2 ** width}")


if __name__ == "__main__":
    # for data1 in ["0110", "1001"]: # ["101011"]:# ["011000100111", "111111000000"]:
    # test1()
    test1()
    winsound.Beep(2500, 5000)
