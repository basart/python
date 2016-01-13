import random
import datetime
import math
import pylab
from matplotlib import mlab
import matplotlib.pyplot as plt

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

def timer_for_sorting_bubble(test_list):
    start = datetime.datetime.now()
    puz(test_list)
    finish = datetime.datetime.now()
    return (finish - start).total_seconds()


def timer_for_quick_sort(test_list):
    start = datetime.datetime.now()
    test_list.sort()
    finish = datetime.datetime.now()
    return (finish - start).total_seconds()



if __name__ == "__main__":
    xlist = mlab.frange(10000, 50000, 10000)
    test_list = []
    for i in range(len(xlist)):
        test_list.append(iter_list(xlist[i]))
    plt.subplot(211)
    ylist = [timer_for_quick_sort(test_list[x/10000-1]) for x in xlist]
    plt.bar(xlist, ylist, 100)
    plt.xticks(xlist)
    plt.yticks(ylist)

    plt.subplot(212)
    ylist = [timer_for_sorting_bubble(test_list[x/10000-1]) for x in xlist]
    plt.bar(xlist, ylist, 100)
    plt.xticks(xlist)
    plt.yticks(ylist)
    plt.show()


