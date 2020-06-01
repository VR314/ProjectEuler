import random

GRID_SIZE = 21  # 1 greater than y x y
grid = [[j*GRID_SIZE + i for i in range(0, GRID_SIZE)]
        for j in range(0, GRID_SIZE)]
# print(grid)

endPoint = GRID_SIZE**2 - 1


def traverse(curr):
    if curr != 0:
        if int(curr / GRID_SIZE) == (GRID_SIZE - 1):  # bottom edge
            return curr+1
        elif curr % (GRID_SIZE) == GRID_SIZE - 1:  # right edge
            return curr + GRID_SIZE

    if random.randint(0, 1) == 0:  # move right
        return curr+1
    else:  # move down
        return curr + GRID_SIZE


path = []
already = []
empty = 0
iterations = 0
while empty < 100:
    curr = 0
    iterations = iterations + 1

    while curr < endPoint:
        curr = traverse(curr)
        path.append(curr)

    if(path not in already):
        already.append(path)
        empty = 0
    else:
        empty = empty + 1

    path = []
    if iterations % 1000 == 0:
        print(str(iterations) + " it, " + str(len(already)))

print(len(already))
