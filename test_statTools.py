import pytest
from statTools import *

#median

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
    assert(median([]) == "")

def test_median_unsortedlst():
    assert(median([1, 9, 3, 6, 8]) == 6)

#lowerQuart

def test_lowerQuart_basic1():
    assert(lowerQuart([1]) == 1)

def test_lowerQuart_basic2():
    assert(lowerQuart([1, 2]) == 1)

def test_lowerQuart_basic3():
    assert(lowerQuart([1, 2, 3]) == 1)

def test_lowerQuart_basic4():
    assert(lowerQuart([1, 2, 3, 4]) == 1.5)

def test_lowerQuart_remainderof1():
    assert(lowerQuart([1, 2, 3, 4, 5]) == 1.5)

def test_lowerQuart_remainderof2():
    assert(lowerQuart([1, 2, 3, 4, 5, 6]) == 2)

def test_lowerQuart_remainderof3():
    assert(lowerQuart([1, 2, 3, 4, 5, 6, 7]) == 2)

def test_lowerQuart_remainderof0pt2():
    assert(lowerQuart([1, 2, 3, 4, 5, 6, 7, 8]) == 2.5)

def test_lowerQuart_emptystr():
    assert(lowerQuart([]) == "")

def test_lowerQuart_unsortedlist():
    assert(lowerQuart([3, 1, 6, 7, 9, 4]) == 3)

#upperQuart

def test_upperQuart_basic1():
    assert(upperQuart([1]) == 1)

def test_upperQuart_basic2():
    assert(upperQuart([1, 2]) == 2)

def test_upperQuart_basic3():
    assert(upperQuart([1, 2, 3]) == 3)

def test_upperQuart_basic4():
    assert(upperQuart([1, 2, 3, 4]) == 3.5)

def test_upperQuart_basic5():
    assert(upperQuart([1, 2, 3, 4, 5]) == 4.5)

def test_upperQuart_biggerlistremainder2():
    assert(upperQuart([1, 2, 3, 4, 5, 6]) == 5)

def test_upperQuart_biggerlistremainder3():
    assert(upperQuart([1, 2, 3, 4, 5, 6, 7]) == 6)

def test_upperQuart_biggerlistremainder0():
    assert(upperQuart([1, 2, 3, 4, 5, 6, 7, 8]) == 6.5)

def test_upperQuart_biggerlistremainder1():
    assert(upperQuart([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 7.5)

def test_upperQuart_emptystr():
    assert(upperQuart([]) is None)

def test_upperQuart_unsortedlist():
    assert(upperQuart([3, 1, 6, 7, 9, 4]) == 7)

def test_upperQuart_notalist():
    with pytest.raises(TypeError) as errmsg:
        upperQuart(1)
    assert ("Error: non-negative int entered" == str(errmsg.value))




#range

def test_range_basic1():
    assert(range([1]) == 1)

def test_range_basic2():
    assert(range([1, 2]) == 1)

def test_range_basic2():
    assert(range([1, 4, 6]) == 5)

def test_range_emptystr():
    assert (range([]) == "")

def test_range_unsortedlist():
    assert (range([5, 7, 1, 3, 9, 4, 10, 25]) == 24)