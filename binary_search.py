import logging
import random
import time

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s')


def binary_search(array: tuple, target: int) -> (int, None):
    left_side, right_side = 0, len(array) - 1
    n = 0
    while left_side <= right_side:
        n += 1
        middle = round((left_side + right_side) / 2)
        if array[middle] == target:
            return middle, n
        else:
            if array[middle] > target:
                right_side = middle - 1
            else:
                left_side = middle + 1
    return None, n


if __name__ == "__main__":
    ar_start = time.process_time()
    lst = tuple(num * random.randint(2, 5) for num in range(10000000))
    ar_stop = time.process_time()
    logging.info('Tuple has been created. Time: %s', ar_stop - ar_start)
    number = lst[random.randint(0, len(lst) - 1)]
    start = time.process_time()
    result, n = binary_search(array=lst, target=number)
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
