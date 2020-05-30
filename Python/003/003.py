import math

"""
*	Problem #: 003
*	Date Attempted: 05/28/20
*	Date Solved: 05/28/20
*
*	What is the largest prime factor of the number 600851475143 ?
*
*	Answer: 6857
"""


def findLargestPrimeNumber(long):
    again = True
    while again:
        again = False
        for i in range(2, int(math.sqrt(long))):
            if long % i == 0:
                print(str(long) + " / " + str(i))
                long = long / i
                again = True
                break
    return long


print(findLargestPrimeNumber(600851475143))
