import math

from n3utils import colorize_bool, colorize_swap


def n3c_sort(data, printable=True, verbose=0):
    _w = len(data)
    _failed = 0
    _ones = 0
    for i in range(_w):
        if data[i] == 1:
            _ones += 1
    _best = [1 for _ in range(_ones)] + [0 for _ in range(_w - _ones)]
    _r = data[:]
    _count = 0
    while _best != _r:
        for t in range(_w - 1):
            if printable:
                print("Marker C10")
            for _ in range(_r[t + 1]):
                message = f"{colorize_swap(_r, t, t + 1)} -> "
                _r[t], _r[t + 1] = _r[t + 1], _r[t]
                message += f"{colorize_swap(_r, t, t + 1)}"
                if verbose > 0:
                    print(message)
                _count += 1
                if printable:
                    print("Marker C11: after marker C10 _r=" + str(_r))
            if _best == _r:
                break
        if _best == _r:
            break
        for t in range(1, _w - 1):
            if printable:
                print("Marker C20")
            for _ in range(_r[t + 1]):
                message = f"{colorize_swap(_r, t - 1, t + 1)} -> "
                _r[t - 1], _r[t + 1] = _r[t + 1], _r[t - 1]
                message += f"{colorize_swap(_r, t - 1, t + 1)}"
                if verbose > 0:
                    print(message)
                _count += 1
                if printable:
                    print("Marker C21: after marker C20 _r=" + str(_r))
        if _count > 2 ** _w:
            _failed += 1
            raise Exception("failed > 0")
    _bits = 0
    _bits += math.ceil(math.log2(_count + 1))
    _bits += math.ceil(math.log2(_w))
    if _w == 1:
        _bits += 1
    result = _bits < _w
    _warning = colorize_bool(result)
    _percent = str(100 * _bits / _w)[0:6].rjust(6, ' ')
    if printable:
        print(
            f"{_percent}, " +
            f"{_warning}, " +
            f"_bits={_bits}, _w={_w}, _count={_count}, _ones={_ones}"
        )
    return result, _percent, _bits, _count, _ones


def n3c_recovery(_width, _count, _one,
                 _max_count_bits=None, printable=True, verbose=0):
    _r = [1 for _ in range(_one)] + [0 for _ in range(_width - _one)]
    if printable:
        print(f"count_of_operations={_count}, count_of_ones={_one}")
        print(f"input_for_recovery_data={_r}")
    while _count > 0:
        for t in range(_width - 1):
            if printable:
                print("Marker D20")
            for _ in range(1 - _r[t + 1]):
                message = f"{colorize_swap(_r, t, t + 1)} -> "
                _r[t], _r[t + 1] = _r[t + 1], _r[t]
                message += f"{colorize_swap(_r, t, t + 1)}"
                if verbose > 0:
                    print(message)
                _count -= 1
                if printable:
                    print("Marker D21: after marker D20 _r=" + str(_r))
            if _count == 0:
                break
        if _count == 0:
            break
        for t in range(1, _width - 1):
            if printable:
                print("Marker D10")
            for _ in range(1 - _r[t + 1]):
                message = f"{colorize_swap(_r, t - 1, t + 1)} -> "
                _r[t - 1], _r[t + 1] = _r[t + 1], _r[t - 1]
                message += f"{colorize_swap(_r, t - 1, t + 1)}"
                _count -= 1
                if verbose > 0:
                    print(message)
                if printable:
                    print("Marker D11: after marker D10 _r=" + str(_r))
            if _count == 0:
                break
    return _r
