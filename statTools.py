
def median(numlist):
    n = len(numlist)
    numlist.sort()

    if n == 0:
        return 0

    if n == 1:
        return numlist[0]

    if n % 2 == 0:
        return ((numlist[n//2]) + (numlist[(n//2)-1]))/2

    else:
        return numlist[(0+(n-1))//2]


