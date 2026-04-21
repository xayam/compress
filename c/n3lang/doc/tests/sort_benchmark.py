from bench import tic, toc
from random import sample

from sorting import insertion_sort, merge_sort, quick_sort


def benchmark(func):

	n = [10 ** 2, 10 ** 3, 10 ** 4, 10 ** 5]

	for i in n:
		unsorted = sample(range(0, i), i)
		tic()
		func(unsorted)
		print("%s(%d)   \t %.4gs" % (func.__name__, i, toc()))


benchmark(insertion_sort)

benchmark(merge_sort)

benchmark(quick_sort)
