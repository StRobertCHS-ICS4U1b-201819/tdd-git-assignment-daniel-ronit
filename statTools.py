
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
        return numlist[(0+(n-1))//2]

def lowerQuart(numlist):
    n = len(numlist)
    numlist.sort()

    if n % 4 == 0:
        return (numlist[n//4] + numlist[(n//4)-1]) / 2

    if n % 4 == 1:
        return (numlist[(n-1)//4] + numlist[(n-1)//4-1]) / 2

    if n % 4 == 2:
        return numlist[(0 + (n//2))//2]

    if n % 4 == 3:
        return numlist[(0 + ((n//2)-1))//2]

