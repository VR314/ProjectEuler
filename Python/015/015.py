import math

"""
*	Problem #: 015
*	Date Attempted: 05/31/20
*	Date Solved: 06/02/20
*
*	How many such routes are there through a 20×20 grid?
*
*	Answer: 137846528820
"""

GRID_SIZE = 21
d = {GRID_SIZE**2 - 1: 1}


def findAns():
    col = GRID_SIZE - 1
    while col > -1:
        for i in range(GRID_SIZE - 1, -1, -1):
            coord = col * GRID_SIZE + i
            d[coord] = calc(coord)
        col = col - 1
    return d[0]


def calc(num):
    if num == GRID_SIZE**2 - 1:
        return 1
    if (num + 1) % GRID_SIZE == 0 or math.floor(num / GRID_SIZE) == GRID_SIZE - 1:
        return 1
    else:
        down = d[num + GRID_SIZE]
        right = d[num + 1]
        return down + right


print(findAns())
