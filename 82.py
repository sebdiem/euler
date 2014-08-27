import numpy as np
import time 

MATRIX = np.loadtxt('matrix82.txt', delimiter=',')
LENGTH = 80
assert MATRIX.shape == (LENGTH, LENGTH)
MOVES = ((-1, 0), (1, 0), (0, 1)) # up, down and right

#MATRIX = np.array([
#        [131,673,234,103,18],
#        [201,96,342,965,150],
#        [630,803,746,422,111],
#        [537,699,497,121,956],
#        [805,732,524,37,331],
#       ])
#LENGTH = 5

def path_cost(path):
    return path[-1][0]

def is_allowed(move, position):
    i, j = position
    di, dj = move
    return 0 <= i+di < LENGTH and 0 <= j+dj < LENGTH

def problem82():
    best_costs = np.zeros(MATRIX.shape)
    best_costs[:,0] = MATRIX[:,0]
    frontier = [(m[0], i, 0) for i, m in enumerate(MATRIX)]
    while len(frontier) > 0:
        current = frontier.pop()
        cost, i, j = current
        if cost <= best_costs[i][j]:
            successors = []
            for move in MOVES:
                if is_allowed(move, (i,j)):
                    di, dj = move
                    next = (cost + MATRIX[i+di, j+dj], i+di, j+dj)
                    best_cost = best_costs[i+di, j+dj]
                    if best_cost == 0 or best_cost > next[0]:
                        best_costs[i+di, j+dj] = next[0]
                        if j+dj < LENGTH-1:
                            successors.append(next)
            frontier.extend(successors)
    return min(best_costs[:,-1])

start = time.time()
print problem82(), ' in %s seconds' % (time.time() - start)
