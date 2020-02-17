"""Write a program that will take one List as input and give a single List
containing multiple Lists with similar Elements as output

Test cases:
    [1, 3, 5, 2, 4, 2, 1, 6]    -->     [[1, 1], [2, 2], [3], [4], [5], [6]]
    [1, 1, 1, 1, 1, 1, 1, 1, 1] -->     [[1, 1, 1, 1, 1, 1, 1, 1, 1]]
    [1, 2, 3, 4, 5, 6, 7, 8]    -->     [[1], [2], [3], [4], [5], [6], [7], [8]]
"""

import collections
import timeit
from statistics import mean, stdev

solution = """\
def solution(input_list: list):
    output_list = []
    get_counter = collections.Counter(sorted(input_list))
    for i, j in get_counter.items():
        output_list.append([i] * j)
    return output_list
"""

comp_solution = """\
def comp_solution(input_list: list):
    get_counter = collections.Counter(sorted(input_list))
    output_list = [[i] * j for i, j in get_counter.items()]
    return output_list
"""

test = """\
if __name__ == '__main__':
    test1 = solution([1, 1, 5, 2, 4, 2, 1, 6])
    test2 = solution([1, 1, 1, 1, 1, 1, 1, 1, 1])
    test3 = solution([1, 2, 3, 4, 5, 6, 7, 8])
    test4 = comp_solution([1, 1, 5, 2, 4, 2, 1, 6])

    print(test1)
    print(test4)
    # print(test2)
    # print(test3)
"""

time_for_solution = timeit.repeat(solution, test, number=100000, repeat=6)
stdeviation_solution = stdev(time_for_solution)

print("mean time for solution: ", mean(time_for_solution), "\t",
      "standard deviation for solution: ", stdev(time_for_solution))
print()

time_for_comp_solution = timeit.repeat(comp_solution, test, number=100000, repeat=6)
stdeviation_comp_solution = stdev(time_for_comp_solution)
print("mean time for comp_solution: ", mean(time_for_comp_solution), "\t",
      "standard deviation for comp_solution: ", stdev(time_for_comp_solution))

print()
print(max(stdeviation_solution, stdeviation_comp_solution))
print(min(stdeviation_solution, stdeviation_comp_solution))
