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


if __name__ == "__main__":
    lst = [random.randint(0, 500) for i in range(950)]
    result = summarize(array=lst)
    count_result = count(array=lst)
    maximum_result = maximum(array=lst, elem=lst[0])
    logging.info("Sum Recursion Algorithm Result --> %s", result)
    logging.info("Count Recursion Algorithm Result --> %s", count_result)
    logging.info("Max Recursion Algorithm Result --> %s", maximum_result)
