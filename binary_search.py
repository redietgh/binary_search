#!/bin/python3


def find_smallest_positive(xs):
    def helper(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        if xs[mid] > 0:
            if mid == 0 or xs[mid - 1] <= 0:
                return mid
            else:
                return helper(left, mid - 1)
        else:
            return helper(mid + 1, right)
    return helper(0, len(xs) - 1)


def count_repeats(xs, x):
    if not xs:
        return 0

    def search_left(left, right):
        if left == right:
            if xs[left] == x:
                return left
            else:
                return None
        result = None
        mid = (left + right) // 2
        if x == xs[mid]:
            result = mid
            if xs[mid - 1] == x and mid != 0:
                right = mid - 1
            else:
                return result
        elif x < xs[mid]:
            left = mid + 1
        else:
            right = mid - 1
        return search_left(left, right)

    def search_right(left, right):
        if left == right:
            if xs[left] == x:
                return left
            else:
                return None
        result = None
        mid = (left + right) // 2
        if x == xs[mid]:
            result = mid
            if xs[mid + 1] == x and ((mid + 1) < len(xs)):
                left = mid + 1
            else:
                return result
        elif x > xs[mid]:
            right = mid - 1
        else:
            left = mid + 1
        return search_right(left, right)

    leftmost_i = search_left(0, len(xs) - 1)
    rightmost_i = search_right(0, len(xs) - 1)
    if leftmost_i is None and rightmost_i is None:
        return 0
    else:
        return (rightmost_i - leftmost_i) + 1


def argmin(f, lo, hi, epsilon=1e-3):
    if hi - lo < epsilon:
        return (hi + lo) / 2
    m1 = lo + (hi - lo) / 3
    m2 = hi - (hi - lo) / 3
    if f(m1) < f(m2):
        return argmin(f, lo, m2, epsilon)
    else:
        return argmin(f, m1, hi, epsilon)
