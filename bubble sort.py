import random
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s]')


def bubble_sort(array):
    replacement = True
    while replacement:
        replacement = False
        for num in range(len(array)):
            if num != 0:
                if array[num - 1] > array[num]:
                    array[num - 1], array[num] = array[num], array[num - 1]
                    replacement = True
    return array


if __name__ == '__main__':
    """
        Bubble Sort Algorithm (1000 size array) - execution time: 0.06135581240000001 seconds.
        Bubble Sort Algorithm (10000 size array) - execution time: 6.534082493599999 seconds.
        Bubble Sort Algorithm (100000 size array) - execution time: 662.0176947316 seconds.
    """
    size_of_arrays = [1e3, 1e4, 1e5]
    number_of_times = 5
    for size in size_of_arrays:
        general_time = 0
        for t in range(number_of_times):
            lst = [random.randint(1, 10) * n for n in range(int(size))]
            start = time.process_time()
            result = bubble_sort(array=lst)
            stop = time.process_time()
            general_time += stop - start
        time_analysis = general_time / number_of_times
        logging.info("Bubble Sort Algorithm (%s size array) - execution time: %s seconds.", int(size), time_analysis)
