# Name:test_statTools.py
# Purpose:
# to test the functions of median, lowerQuart, upperQuart, and range
#
# Author:    Ronit B.
#
# Created:   11/11/2018

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
   assert(median([]) is None)

def test_median_unsortedlst():
   assert(median([1, 9, 3, 6, 8]) == 6)

def test_median_notalist():
   with pytest.raises(TypeError) as errmsg:
       median(1)
   assert ("Error: non-list value entered" == str(errmsg.value))

def test_median_listofstrings():
   with pytest.raises(TypeError) as errmsg:
       median(["a", "e", "i"])
   assert ("Error: non-list value entered" == str(errmsg.value))


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

def test_lowerQuart_emptylist():
   assert(lowerQuart([]) is None)

def test_lowerQuart_unsortedlist():
   assert(lowerQuart([3, 1, 6, 7, 9, 4]) == 3)

def test_lowerQuart_notalist():
   with pytest.raises(TypeError) as errmsg:
       lowerQuart(1)
   assert ("Error: non-list value entered" == str(errmsg.value))

def test_lowerQuart_listofstrings():
   with pytest.raises(TypeError) as errmsg:
       lowerQuart(["a", "e", "i"])
   assert ("Error: non-list value entered" == str(errmsg.value))

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

def test_upperQuart_emptylist():
   assert(upperQuart([]) is None)

def test_upperQuart_unsortedlist():
   assert(upperQuart([3, 1, 6, 7, 9, 4]) == 7)

def test_upperQuart_notalist():
   with pytest.raises(TypeError) as errmsg:
       upperQuart(1)
   assert ("Error: non-int list value entered" == str(errmsg.value))

def test_upperQuart_listofstrings():
   with pytest.raises(TypeError) as errmsg:
       upperQuart(["a", "e", "i"])
   assert ("Error: non-int list value entered" == str(errmsg.value))

#range

def test_range_basic1():
   assert(range([1]) == 1)

def test_range_basic2():
   assert(range([1, 4, 6]) == 5)

def test_range_emptylist():
   assert (range([]) is None)

def test_range_unsortedlist():
   assert (range([5, 7, 1, 3, 9, 4, 10, 25]) == 24)

def test_range_notalist():
   with pytest.raises(TypeError) as errmsg:
       range(1)
   assert ("Error: non-list value entered" == str(errmsg.value))

def test_range_listofstrings():
   with pytest.raises(TypeError) as errmsg:
       range(["a", "e", "o"])
   assert ("Error: non-list value entered" == str(errmsg.value))

