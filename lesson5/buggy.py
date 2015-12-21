def multiple(*numbers):
    i = 0
    res = 1
    while i <= len(numbers) - 1:
        res = numbers[i] * res
        i += 1
    return res


if __name__ == "__main__":
    assert multiple(0, 1) == 0
    assert multiple(1, 2, 3) == 6
    assert multiple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 3628800
    print('all test passed')
    