import logging
import random
import time

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s')


def selection_sort(array):
    for t in range(len(array)):
        array_slice, min_index = array[t:], 0
        for i, v in enumerate(array_slice):
            if array_slice[i] < array_slice[min_index]:
                min_index = i
        array.insert(t, array.pop(array.index(array_slice[min_index])))
    return array


if __name__ == "__main__":

    """
    Selection Sort Algorithm (1000 size array) - execution time: 0.033666246999999996 seconds.
    Selection Sort Algorithm (10000 size array) - execution time: 3.2779681409999997 seconds.
    Selection Sort Algorithm (100000 size array) - execution time: 355.438230902 seconds.
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
