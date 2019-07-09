import logging
import random
import time

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

    """
    Selection Sort Algorithm (2000 size array) - execution time: 0.09047635200000001 seconds.
    Selection Sort Algorithm (20000 size array) - execution time: 9.488463571 seconds.
    Selection Sort Algorithm (100000 size array) - execution time: 240.28286130799998 seconds."""

    lst = [random.randint(0, 500) for num in range(100000)]
    size = len(lst)
    arr = lst[:]
    start = time.process_time()
    selection_sort(array=lst)
    stop = time.process_time()
    logging.info(
        "Selection Sort Algorithm (%s size array) - execution time: %s seconds.", size, stop - start
    )