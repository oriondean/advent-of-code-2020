from typing import List
import functools


def find_sum_of_two(list: list[int], sum: int):
    for itemA in list:
        for itemB in list:
            if itemA + itemB == sum:
                return [itemA, itemB]


def find_sum_of_three(list: list[int], sum: int):
    for itemA in list:
        for itemB in list:
            for itemC in list:
                if itemA + itemB + itemC == sum:
                    return [itemA, itemB, itemC]

if __name__ == '__main__':
    with open('input.txt') as file:
        input: list[str] = file.read().split()
        file.close()

    expenses: list[int] = list(map(int, input))

    resultOne: [int, int] = find_sum_of_two(expenses, 2020)
    print('Part one', functools.reduce(lambda a, b: a*b, resultOne))

    resultTwo: [int, int, int] = find_sum_of_three(expenses, 2020)
    print('Part two', functools.reduce(lambda a, b: a*b, resultTwo))


