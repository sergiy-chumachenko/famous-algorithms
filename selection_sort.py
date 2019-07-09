import logging
import random

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s')


def get_min_item_index(array):
    min_item_index = 0
    for index in range(1, len(array)):
        if array[index] <= array[min_item_index]:
            min_item_index = index
    return min_item_index


def selection_sort(array):
    sorted_lst = []
    for num in range(len(array)):
        min_item_index = get_min_item_index(array=array)
        sorted_lst.append(array.pop(min_item_index))
    return sorted_lst


if __name__ == "__main__":
    lst = [random.randint(0, 100) for num in range(20)]
    print(lst)
    print(selection_sort(array=lst))
