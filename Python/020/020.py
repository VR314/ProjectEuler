import math

"""
*	Problem #: 020
*	Date Attempted: 06/04/20
*	Date Solved: 06/04/20
*
*	Find the sum of the digits in the number 100!
*
*	Answer: 648 
"""


def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)


def getDigit(x, i):
    return int(str(x)[i])


def sumDigits(x):
    length = len(str(x))
    sum = 0
    for i in range(0, length):
        sum = sum + getDigit(x, i)
    return sum


print(sumDigits(factorial(100)))
