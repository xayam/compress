from time import time

mark = 0


def tic():
    global mark
    mark = time()


def toc():
    global mark
    elapsed = time() - mark
    return elapsed
