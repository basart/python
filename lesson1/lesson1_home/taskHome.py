if __name__ == "__main__":
    list_number = [0, 1, 2, 3, 4, 5]
    sum_list_number = 0
    index_number_in_list = 1
    try:
        while index_number_in_list <= len(list_number) - 1:
            sum_list_number += list_number[index_number_in_list]
            index_number_in_list += 2
        last_number = list_number[-1]
        print(sum_list_number * last_number)
    except IndexError:
        print(0)

# print listNumber[1]
# if listNumber:
#     print(sum(listNumber[1: len(listNumber): 2])*listNumber[-1])
# else:
#     print(0)

