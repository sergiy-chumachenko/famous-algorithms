import random
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s]')


def binary_search_recursion(array, target, n):
    mid_index = int(len(array) / 2)
    if array[mid_index] == target:
        return array[mid_index], n + 1
    elif array[mid_index] > target:
        return binary_search_recursion(array=array[:mid_index], target=target, n=n + 1)
    else:
        return binary_search_recursion(array=array[mid_index + 1:], target=target, n=n + 1)


if __name__ == "__main__":
    """
    Array has been created. Time: 94.00832736599999
    Target '42384603' on 42384603 position in array (100000000 elem). 
    23 attempts has been made. 
    Time: 3.1769464940000063 seconds.
    """
    ar_start = time.process_time()
    lst = sorted(tuple(num * random.randint(2, 5) for num in range(100000000)))
    ar_stop = time.process_time()
    logging.info('Tuple has been created. Time: %s', ar_stop - ar_start)
    number = lst[random.randint(0, len(lst) - 1)]
    start = time.process_time()
    result, n = binary_search_recursion(array=lst, target=number, n=0)
    stop = time.process_time()

    if result:
        logging.info(
            "Target '%s' on %s position in array. %s attempts has been made. Time: %s seconds.",
            number, result, n, stop - start
        )
    else:
        logging.info(
            "Target '%s' not found. %s attempts has been made. Time: %s seconds.", number, n, stop - start
        )
