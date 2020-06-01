import math

"""
*	Problem #: 016
*	Date Attempted: 05/30/20
*	Date Solved: 05/30/20
*
*	What is the sum of the digits of the number 2^1000?
*
*	Answer: 1366 
"""


def getDigit(x, orig):
    return math.floor((orig % 10**x) / 10**(x-1))


const = 2**1000
print(const/1.0)

sum = 0
for i in range(0, 10000):
    sum = sum + getDigit(i, const)

print(sum)
