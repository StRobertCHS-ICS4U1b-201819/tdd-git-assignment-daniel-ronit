# Name:statTools.py
# Purpose:
# to code the functions of median, lowerQuart, upperQuart, and range
#
# Author:    Ronit B.
#
# Created:   11/11/2018

def median(numlist):
   '''
   :param numlist: list of integers
   :return: middle index value of a sorted list
   '''
   try:
       #  variable for length of list
       n = len(numlist)

       # variable made for Type Error to be raised
       exception_raiser = sum(numlist)

       # sorts the list
       numlist.sort()

       # empty list case
       if n == 0:
           return None

       if n % 2 == 0:
           # when even amount of numbers, adds two center numbers and divides by 2
           return ((numlist[n//2]) + (numlist[(n//2)-1])) / 2

       else:
           # when odd number of numbers, divides list by 2 and finds middle
           return numlist[(n-1) // 2]

   except TypeError:
       raise TypeError("Error: non-list value entered")


def lowerQuart(numlist):
   '''
   :param numlist: list of integers
   :return: middle index value of lower half of list
   '''
   try:
       #  variable for length of list
       n = len(numlist)

       # variable made for Type Error to be raised
       exception_raiser = sum(numlist)

       # sorts the list
       numlist.sort()

       # empty list case
       if n == 0:
           return None

       if n % 4 == 0 or n % 4 == 1:
           # add two numbers lowerQuart is between and divide by 2
           return (numlist[n//4] + numlist[(n//4) - 1]) / 2

       else:
           # index number: divides list by 2, moves 1 left for middle, then divides by 2 again
           return numlist[((n//2) - 1) // 2]

   except TypeError:
       raise TypeError("Error: non-list value entered")

def upperQuart(numlist):
   '''
   :param numlist: list of integers
   :return: middle index value of upper half of list
   '''
   try:
       #  variable for length of list
       n = len(numlist)

       #variable made for Type Error to be raised
       exception_raiser = sum(numlist)

       # sorts the list
       numlist.sort()

       # empty list case
       if n == 0:
           return None

       # list with one number
       if n == 1:
           return numlist[0]

       if n % 4 == 0 or n % 4 == 1:
           # add two numbers upperQuart is between and divide by 2
           return (numlist[(n-1) - (n//4)+1] + numlist[(n-1) - (n//4)]) / 2

       # if n mod 4 == 2 or if n mod 4 == 3
       else:
           # subtract 1/4 of list length by length of list and use as index of list
           return numlist[(n-1) - (n//4)]

   except TypeError:
       # raise error when anything other than a list is entered
       raise TypeError("Error: non-int list value entered")

def range(numlist):
   '''
   :param numlist: list of integers
   :return: highest number minus the lowest number of a sorted list
   '''
   try:
       #  variable for length of list
       n = len(numlist)

       # sorts the list
       numlist.sort()

       # empty list case
       if n == 0:
           return None

       # list with one number
       if n == 1:
           return numlist[0]

       else:
           # highest number minus the lowest number
           return numlist[n-1] - numlist[0]

   except TypeError:
       #raise error when anything other than a list is entered
       raise TypeError('Error: non-list value entered')
