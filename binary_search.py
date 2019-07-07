import logging

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]:[%(levelname)s]:[MESSAGE] %(message)s')


def binary_search(array: list, target: int) -> (int, None):
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
    lst = [num for num in range(0, 240000)]
    number = 11
    result, n = binary_search(array=lst, target=number)
    if result:
        logging.info("Target '%s' on %s position in array. %s attempts has been made" % (number, result, n))
    else:
        logging.info("Target '%s' not found,  %s attempts has been made" % (number, n))
