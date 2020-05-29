"""
*	Problem #: 004
*	Date Attempted: 05/28/20
*	Date Solved: 05/28/20
*
*	Find the largest palindrome made from the product of two 3-digit numbers.
*
*	Answer: 906609
"""

for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        number = str(x * y)
        if len(number) == 6 and number[5] == number[0] and number[4] == number[1] and number[3] == number[2]:
            print(x * y)
