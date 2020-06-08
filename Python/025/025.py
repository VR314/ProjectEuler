
"""
*	Problem #: 025
*	Date Attempted: 06/07/20
*	Date Solved: 06/07/20
*
*	What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
*
*	Answer: 4782
"""


def fib():
    a = 1
    b = 1
    c = 2
    index = 3
    while len(str(c)) < 1000:
        index += 1
        a = b
        b = c
        c += a
    return index


print(fib())
