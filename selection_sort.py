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
    Selection Sort Algorithm (1000 size array) - execution time: 0.023112136999999998 seconds.
    Selection Sort Algorithm (10000 size array) - execution time: 2.391768241 seconds.
    Selection Sort Algorithm (100000 size array) - execution time: 260.371566086 seconds.
    """

    for t in 1000, 10000, 100000:
        lst = [random.randint(0, 500) for num in range(t)]
        size = len(lst)
        arr = lst[:]
        start = time.process_time()
        selection_sort(array=lst)
        stop = time.process_time()
        logging.info(
            "Selection Sort Algorithm (%s size array) - execution time: %s seconds.", size, stop - start
        )