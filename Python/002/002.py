"""
*	Problem #: 002
*	Date Attempted: 05/28/20
*	Date Solved: 05/28/20
*
*	By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
*   find the sum of the even-valued terms.
*
*	Answer: 4613732
"""

def nextFib(prev, prev2):
    return prev + prev2

a = 1
b = 1
x = 0
sum = 0
while x < 4000000:
    a = b
    b = x
    x = nextFib(a, b)
    if x % 2 == 0:
        sum = sum + x

print(sum)
