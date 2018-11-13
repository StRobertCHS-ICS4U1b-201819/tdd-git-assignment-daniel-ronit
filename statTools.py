
def median(numlist):
    n = len(numlist)
    numlist.sort()

    if n == 0:
        return ""

    if n == 1:
        return numlist[0]

    if n % 2 == 0:
        return ((numlist[n//2]) + (numlist[(n//2)-1]))/2

    else:
        return numlist[(n-1)//2]

def lowerQuart(numlist):
    n = len(numlist)
    numlist.sort()

    if n == 0:
        return ""

    if n % 4 == 0 or n % 4 == 1:
        return (numlist[n//4] + numlist[(n // 4) - 1]) / 2

    else:
        return numlist[((n//2) - 1)//2]

def upperQuart(numlist):
    try:
        n = len(numlist)
        exception_raiser = sum(numlist)
        numlist.sort()

        if n == 0:
            return None

        if n == 1:
            return numlist[0]

        if n % 4 == 0 or n % 4 == 1:
            return (numlist[(n-1)-(n//4)+1] + numlist[(n-1)-(n//4)])/2

        else:
            return numlist[(n-1) - (n//4)]
    except TypeError:
        raise TypeError("Error: non-negative int entered")


def range(numlist):
    n = len(numlist)
    numlist.sort()

    if n == 0:
        return ""

    if n == 1:
        return numlist[0]

    else:
        return numlist[n-1] - numlist[0]