import random
import logging

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s]')


def summarize(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + summarize(array[1:])


def count(array):
    if len(array) == 0:
        return 0
    else:
        return 1 + count(array[1:])


def maximum(array, elem):
    if len(array) == 0:
        return elem
    else:
        if array[0] > elem:
            elem = array[0]
        return maximum(array=array[1:], elem=elem)


def maximum2(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    else:
        smax = maximum2(array[1:])
    return array[0] if array[0] > smax else smax


if __name__ == "__main__":
    lst = [random.randint(0, 500) for i in range(950)]
    result = summarize(array=lst)
    count_result = count(array=lst)
    maximum_result = maximum(array=lst, elem=lst[0])
    maximum2_result = maximum2(array=lst)
    logging.info("Sum Recursion Algorithm Result --> %s", result)
    logging.info("Count Recursion Algorithm Result --> %s", count_result)
    logging.info("Max Recursion Algorithm Result --> %s", maximum_result)
    logging.info("Max Ver.2 Recursion Algorithm Result --> %s", maximum2_result)
