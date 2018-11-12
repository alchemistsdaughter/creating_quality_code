# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:23:13 2018

@author: anna.whitehouse
"""

# =============================================================================
# import doctest
# 
# doctest.testmod()
# =============================================================================


def sum_items(L):
    """ (list of number) -> number
  
    Return the sum of the items in L.
    """

    total = 0
 
    for item in L:
        total = item

    return total

L = [1, 0, 1]
print(sum_items(L))
