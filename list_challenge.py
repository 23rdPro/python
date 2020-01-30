"""Write a program that will take one List as input and give a single List
containing multiple Lists with similar Elements as output

Test cases:
    [1, 3, 5, 2, 4, 2, 1, 6]    -->     [[1, 1], [2, 2], [3], [4], [5], [6]]
    [1, 1, 1, 1, 1, 1, 1, 1, 1] -->     [[1, 1, 1, 1, 1, 1, 1, 1, 1]]
    [1, 2, 3, 4, 5, 6, 7, 8]    -->     [[1], [2], [3], [4], [5], [6], [7], [8]]
"""

import collections


def solution(input_list: list):
    output_list = []
    get_counter = collections.Counter(sorted(input_list))
    for i, j in get_counter.items():
        output_list.append([i] * j)
    return output_list


if __name__ == '__main__':
    test1 = solution([1, 1, 5, 2, 4, 2, 1, 6])
    test2 = solution([1, 1, 1, 1, 1, 1, 1, 1, 1])
    test3 = solution([1, 2, 3, 4, 5, 6, 7, 8])

    print(test1)
    print(test2)
    print(test3)
