import random
import logging


logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s]')


def summarize(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + summarize(array[1:])


if __name__ == "__main__":
    lst = [random.randint(0, 500) for i in range(950)]
    result = summarize(array=lst)
    logging.info("Sum Recursion Algorithm Result --> %s", result)
