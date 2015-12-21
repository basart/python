import datetime

def binary_search(list_, value):
    """This function performs a binary search.
    """
    first = 0
    last = len(list_) - 1

    while first <= last:
        middle = first + (last - first) // 2
        if value == list_[middle]:
            return middle
        elif value < list_[middle]:
            last = middle - 1
        else:
            first = middle + 1
    return None


def linear_search(list_, value):
    for i, item in enumerate(list_):
        if item == value:
            return i
    return None


if __name__ == "__main__":
    list_ = range(10**8)
    item_list = 10**8 - 1
    start = datetime.datetime.now()
    binary_search(list_, item_list)
    finish = datetime.datetime.now()
    print(finish - start)
    #assert binary_search(range(3), 2) ==

    start = datetime.datetime.now()
    linear_search(list_, item_list)
    finish = datetime.datetime.now()

    print(finish - start)
