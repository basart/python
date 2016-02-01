import random
import datetime
import math
import pylab
from matplotlib import mlab
import matplotlib.pyplot as plt


def average_value(func_for_surting):
    def wrapper(test_list):
        runtime_sorting = []
        for number_current_test in range(5):
            runtime_sorting.append(func_for_surting(test_list))
        runtime_sorting.sort()
        average_execution_time_of_sorting = sum(runtime_sorting[1:-1]) / 3
        return average_execution_time_of_sorting
    return wrapper

def iter_list(count_number):
    test_list = []
    for item in range(count_number):
        test_list.append(random.choice(range(1000)))
    return test_list

def puz(list_):
    for i in range(len(list_) - 1):
        for j in range(len(list_) - i - 1):
            if list_[j] > list_[j+1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]

@average_value
def timer_for_sorting_bubble(list_for_sorting):
    start = datetime.datetime.now()
    puz(list_for_sorting)
    finish = datetime.datetime.now()
    return (finish - start).total_seconds()

@average_value
def timer_for_quick_sort(list_for_sorting):
    start = datetime.datetime.now()
    list_for_sorting.sort()
    finish = datetime.datetime.now()
    return (finish - start).total_seconds()


if __name__ == "__main__":
    xlist = mlab.frange(1000, 5000, 1000)
    test_list = []
    for i in range(len(xlist)):
        test_list.append(iter_list(xlist[i]))

    plt.subplot(211)
    ylist = [timer_for_quick_sort(test_list[x/1000-1]) for x in xlist]
    plt.bar(xlist, ylist, 100)
    plt.xticks(xlist)
    plt.yticks(ylist)

    plt.subplot(212)
    ylist = [timer_for_sorting_bubble(test_list[x/1000-1]) for x in xlist]
    plt.bar(xlist, ylist, 100)
    plt.xticks(xlist)
    plt.yticks(ylist)
    plt.show()




