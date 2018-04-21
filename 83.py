import argparse
from collections import OrderedDict
from math import floor
from operator import itemgetter

def path_sum(costs_list):
    """Solve minimum cost path.
        Args:
            costs_list: list, the matrix of costs represented as a list
    """
    matrix_size = len(costs_list) ** 0.5
    assert int(matrix_size) == matrix_size, "Invalid matrix data"
    matrix_size = int(matrix_size)

    frontier = OrderedDict([(0, costs_list[0])])
    explored = dict([(0, costs_list[0])])
    best = None

    while frontier:
        current_idx, current_cost = frontier.popitem(last=False)
        explored[current_idx] = current_cost
        candidates = [
            (i, current_cost + costs_list[i])
            for i in list_next(current_idx, matrix_size)
        ]
        for candidate_idx, candidate_cost in candidates:
            if (
                explored.get(candidate_idx, candidate_cost + 1) <= candidate_cost or
                (candidate_idx in frontier and frontier[candidate_idx] <= candidate_cost)
            ):
                continue
            frontier[candidate_idx] = candidate_cost
            if candidate_idx == len(costs_list) - 1:
                best = candidate_cost

        frontier = OrderedDict(sorted(frontier.items(), key=itemgetter(1)))

        if not frontier:
            return best


def list_next(idx, matrix_size):
    ret = []
    if floor((idx - 1) / matrix_size) == floor(idx / matrix_size):
        ret.append(idx - 1)
    if floor((idx + 1) / matrix_size) == floor(idx / matrix_size):
        ret.append(idx + 1)
    if idx + matrix_size < matrix_size ** 2:
        ret.append(idx + matrix_size)
    if idx - matrix_size > -1:
        ret.append(idx - matrix_size)
    return ret


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solve https://projecteuler.net/problem=83')
    parser.add_argument('file_name', type=str, help='File containing the matrix to work on (csv format).')

    args = parser.parse_args()
    with open(args.file_name, mode='r', encoding='utf-8') as f:
        print(path_sum([int(cost.strip()) for line in f for cost in line.split(',')]))
