import math


def insertion_sort(m):
    """
    Public: Sorts a list using the insertion sort algorithm.

    m - The unsorted list.

    Examples

        insertion_sort([4,7,8,3,2,9,1])
        # => [1,2,3,4,7,8,9]

    Worst Case: O(n^2)

    Returns the sorted list.
    """

    for j in range(1, len(m)):
        key = m[j]
        i = j - 1

        # shift everything greater than 'key' to it's right
        while i >= 0 and m[i] > key:
            m[i + 1] = m[i]
            i = i - 1

        m[i + 1] = key

    return m


def merge_sort(m):
    """
    Public: Sorts a list using the merge sort algorithm.

    m - The unsorted list.

    Examples

        merge_sort([4,7,8,3,2,9,1])
        # => [1,2,3,4,7,8,9]

    Worst Case: O(n*Log(n))

    Returns the sorted list.
    """

    length = len(m)

    if length == 1:
        return m

    mid = int(math.floor(length / 2))

    left = merge_sort(m[0:mid])
    right = merge_sort(m[mid:length])

    return merge(left, right)


def merge(left, right):
    """
    Public: Merges two sorted lists.

    left  - A sorted list.
    right - A sorted list.

    Examples

        merge([2,4],[1,6])
        # => [1,2,4,6]

    Returns the sorted list post merge.
    """

    merged = []

    # while at least one list has elements
    while left or right:

        if left and right:
            if left[0] <= right[0]:
                key = left.pop(0)
            else:
                key = right.pop(0)
        elif left:
            key = left.pop(0)
        else:
            key = right.pop(0)

        merged.append(key)

    return merged


def quick_sort(m):
    """
    Public: Sorts a list using the quick sort algorithm.

    m - The unsorted list.

    Examples

        quick_sort([4,7,8,3,2,9,1])
        # => [1,2,3,4,7,8,9]

    Worst Case: O(n^2)

    Returns the sorted list.
    """

    if len(m) <= 1:
        return m

    pivot = m.pop()
    less = []
    gr8t = []

    for i in m:
        if i <= pivot:
            less.append(i)
        else:
            gr8t.append(i)

    return quick_sort(less) + [pivot] + quick_sort(gr8t)
