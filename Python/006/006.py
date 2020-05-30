"""
*	Problem #: 006
*	Date Attempted: 05/29/20
*	Date Solved: 05/29/20
*
*	Find the difference between the sum of the squares of the first one hundred natural numbers 
*   and the square of the sum.
*
*	Answer: 25164150
"""

sum1 = 1
sum2 = 1
for n in range(2, 101):
    sum1 = sum1 + (n**2)
    sum2 = sum2 + n
sum2 = sum2**2
print(sum2 - sum1)
