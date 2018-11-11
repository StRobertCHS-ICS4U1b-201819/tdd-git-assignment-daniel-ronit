import pytest
from statTools import *

def test_median_basic1():
    assert(median([1]) == 1)

def test_median_basic2():
    assert(median([1, 2]) == 1.5)

def test_median_basic3():
    assert(median([1, 2, 3]) == 2)

def test_median_basic4():
    assert(median([1, 2, 3, 4]) == 2.5)

def test_median_basic5():
    assert(median([1, 2, 3, 4, 5]) == 3)

def test_median_emptystr():
    assert(median([]) == 0)

def test_median_unsortedlst():
    assert(median([1, 9, 3, 6, 8]) == 6)