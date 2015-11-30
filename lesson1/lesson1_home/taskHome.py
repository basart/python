listNumber = [1, 3, 4, 6, 5, 4]
oddElements = listNumber[1: len(listNumber): 2]

print(oddElements)
if bool(oddElements):
    print(reduce(lambda res, x: res*x, oddElements, 1))
else:
    print(0)
