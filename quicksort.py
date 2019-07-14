import time
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s')


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        support = random.randint(0, len(array)-1)
        less, greater, equal = [], [], []
        elem = array.pop(support)
        for index in range(len(array)):
            if array[index] < elem:
                less.append(array[index])
            else:
                greater.append(array[index])
        return quicksort(array=less) + [elem] + quicksort(array=greater)


if __name__ == "__main__":
    """
    Selection Sort Algorithm (10000 size array) - execution time: 0.023021002600000003 seconds.
    Selection Sort Algorithm (100000 size array) - execution time: 0.2746743168000001 seconds.
    Selection Sort Algorithm (1000000 size array) - execution time: 3.8669074096000005 seconds.
    Selection Sort Algorithm (10000000 size array) - execution time: 52.66650071419999 seconds.
    """
    size_of_arrays = [10e3, 10e4, 10e5, 10e6]
    number_of_times = 5
    for size in size_of_arrays:
        general_time = 0
        for t in range(number_of_times):
            lst = [random.randint(1, 10) * n for n in range(int(size))]
            start = time.process_time()
            result = quicksort(array=lst)
            stop = time.process_time()
            general_time += stop - start
        time_analysis = general_time / number_of_times
        logging.info("Selection Sort Algorithm (%s size array) - execution time: %s seconds.", int(size), time_analysis)
