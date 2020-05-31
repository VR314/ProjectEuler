
"""
*	Problem #: 014
*	Date Attempted: 05/30/20
*	Date Solved: 05/30/20
*
*	Which starting number, under one million, produces the longest chain?
*
*	Answer: 837799
"""


def nextStep(x):
    if x % 2 == 0:
        return x/2
    else:
        return 3*x + 1


d = {1: 1, 2: 2, 3: 7, 4: 3}


def lengthOfChain(x):
    if x in d:
        return d[x]
    curr = x
    count = 0
    while (curr := nextStep(curr)) != 1:
        count = count + 1
        if curr in d:
            return d[curr] + count
    d[x] = count
    return count


longest = (0, 0)
for i in range(1, 1000000):
    length = lengthOfChain(i)
    print(str(i) + ": " + str(length))
    if length > longest[0]:
        longest = (length, i)

print(longest[1])
