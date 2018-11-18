# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:03:48 2018

@author: anna.whitehouse
"""
import math


def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(20)
    1
    >>> num_buses(50)
    1
    """
    num = math.ceil(n / 50)
    return num


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0.0, 0.0)
    >>> stock_price_summary([-2, -0.01, -.9])
    (0.0, -2.91)
    >>> stock_price_summary([2, 0.01, .9, 0])
    (2.91, 0.0)
    """
    stock_changes = []
    neg_sum = 0.0
    pos_sum = 0.0
    for num in price_changes:
        if num < 0:
            neg_sum += num
        if num >= 0:
            pos_sum += num
    stock_changes.append(pos_sum)
    stock_changes.append(neg_sum)
    return tuple(stock_changes)

print(stock_price_summary([-2, -0.01, -.9]))

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    [5, 6, 3, 4, 1, 2]
    """
    if len(L) == 0:
        return L
    if k == 0:
        return L
    else:
        L[:k], L[-k:] = L[-k:], L[:k]
    return L
swap_k([1, 2, 3, 4, 5, 6, 7], 0)


# =============================================================================
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
# =============================================================================

