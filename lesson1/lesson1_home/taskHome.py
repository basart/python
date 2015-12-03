listNumber = [0, 1, 2, 3, 4, 5]
if listNumber:
    print(sum(listNumber[1: len(listNumber): 2])*listNumber[-1])
else:
    print(0)

