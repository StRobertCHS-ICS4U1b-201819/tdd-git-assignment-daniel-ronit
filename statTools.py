
def median(listofnums):
    n = len(listofnums)

    if n == 1:
        return listofnums[0]

    if n % 2 == 0:
        return (listofnums[n//2] + listofnums[(n//2)-1])/2

    else:
        return listofnums[(0+(n-1))//2]
