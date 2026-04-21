import math
import pprint
import sys
from functools import reduce


def n3c_limit(width=32) -> int:
    assert width > 0
    limit = width
    while True:
        old_limit = limit
        limit = 4 * math.ceil(math.log2(limit)) + 2
        if limit == old_limit:
            break
    return limit


def n3c_get_path_by_name(name: int = 0, width: int = 32) -> list:
    limit = n3c_limit(width)
    # print(width, name)
    assert name >= 0
    passenger = name
    paths = [0]
    destination = passenger
    if passenger == 0:
        paths.append(limit)
        return paths
    else:
        if passenger == limit:
            pass
        else:
            paths = [destination]
    while True:
        destination = 4 * math.ceil(math.log2(destination)) + 2
        paths.append(destination)
        if destination == limit:
            break
    return paths


def n3c_get_new_name(old_name: int, width=32) -> list:
    return [old_name] + n3c_get_path_by_name(old_name, width)


def n3c_paths(name: int = 0, width: int = 32, verbose=0) -> list:
    assert width > 0
    assert 0 <= name <= width
    result = []
    if name == 0:
        for i in range(width):
            paths = n3c_get_new_name(i)
            len_paths = len(paths)
            len_set_paths = len(set(paths))
            assert len_paths - len_set_paths == 1
            result.append(paths)
        if verbose > 0:
            pprint.pprint(result)
        assert len(result) == width
        return result
    else:
        paths = n3c_get_new_name(name)
        len_paths = len(paths)
        len_set_paths = len(set(paths))
        if verbose > 0:
            print(paths, len_paths, len_set_paths)
        assert len_paths - len_set_paths == 1
        return paths


def main(maximum: int):
    result = []
    for width in range(1, maximum):
        limit = n3c_limit(width)
        paths = n3c_paths(width=width, verbose=0)
        result.append(paths)
        assert paths
    pprint.pprint(result, width=len(result[-1]) ** 2 - len(result[-1][-1]) ** 2)
        # print(paths)
        # if type(paths[0]) is list:
            # (paths[-1][-1] == limit):
            # (len(paths[0]) > 2) and \
            # (paths[0][0] == 0) and \
            # assert len(paths[0]) - len(set(paths[0])) == 1
            # continue
        # if not type(paths[0]) is list:
        #     assert len(paths) - len(set(paths)) == 1


def test():
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
              37, 41, 43, 47, 53, 59, 61, 67, 71,
              73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131,
              137, 139, 149, 151, 157,
              163, 167, 173, 179, 181,
              191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241,
              251, 257, 263, 269, 271, 277,
              281, 283, 293, 307, 311, 313,
              317, 331, 337, 347, 349, 353,
              359, 367, 373, 379, 383, 389, 397,
              401,
              409, 419, 421, 431, 433,
              439, 443, 449, 457, 461, 463,
              467, 479, 487, 491, 499, 503,
              509, 521, 523, 541, 547, 557,
              563, 569, 571, 577, 587, 593,
              599, 601, 607, 613, 617,
              619, 631, 641, 643, 647, 653, 659,
              661, 673, 677, 683, 691,
              701, 709, 719, 727, 733, 739, 743,
              751, 757, 761, 769, 773,
              787, 797, 809, 811, 821, 823, 827,
              829, 839, 853, 857, 859,
              863, 877, 881, 883, 887, 907, 911,
              919, 929, 937, 941, 947,
              953, 967, 971, 977, 983, 991, 997,
              1009, 1013, 1019, 1021, 1031, 1033,
              1039, 1049, 1051, 1061, 1063, 1069,
              1087, 1091, 1093, 1097, 1103, 1109,
              1117, 1123, 1129, 1151, 1153, 1163,
              1171, 1181, 1187, 1193, 1201, 1213,
              1217, 1223, 1229, 1231, 1237, 1249,
              1259, 1277, 1279, 1283, 1289, 1291,
              1297, 1301, 1303, 1307, 1319, 1321,
              1327, 1361, 1367, 1373, 1381, 1399,
              1409, 1423, 1427, 1429, 1433, 1439,
              1447, 1451, 1453, 1459, 1471, 1481,
              1483, 1487, 1489, 1493, 1499, 1511,
              ]
    r = 2 ** 32 - 1
    m = 1
    old_r = 1
    s = "2 ** 32 - 1 - "
    c = [[]]
    summa = 0
    print(str(2 ** 32 - 1 - reduce(lambda x, y: x * y,
                                   [3, 5, 7, 11, 13, 17, 19, 23, 29])))
    print(len(primes))
    p = 0
    while r != 3:
        new_m = m * primes[p]
        r = r - new_m
        if r < 0:
            r = m
            summa += r
            m = 1
            s = f"{s} - {r} "
            print(s)
            s = f"{r}"
            c.append([])
            p = 0
        else:
            c[-1].append(primes[p])
            s = f"{s} {primes[p]}*"
            p += 1
            m = new_m
    print(summa)
    print(c)
    summa2 = 3
    for i in range(len(c[:-2])):
        product = 1
        for j in range(len(c[i])):
            product *= c[i][j]
        summa2 += product
    print(summa2)


if __name__ == "__main__":
    main(maximum=64)

    # n3c_paths(name=0, width=32)
