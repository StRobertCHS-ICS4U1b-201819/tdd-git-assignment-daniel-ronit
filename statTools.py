
def median(listofnums):

    if (len(listofnums) == 1):
        return listofnums[0]

    if (len(listofnums) == 2):
        return (listofnums[1] + listofnums[0])//2

    if (len(listofnums) == 3):
        return listofnums[(0 + (len(listofnums)-1))//2]
