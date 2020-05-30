"""
*	Problem #: 005
*	Date Attempted: 05/29/20
*	Date Solved: 05/29/20
*
*	What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*
*	Answer: 232792560
"""

primes = [2, 3, 5, 7, 11, 13, 17, 19]
exponents = [1, 1, 1, 1, 1, 1, 1, 1]
product = 1
for i in range(0, len(primes)):
    while primes[i] ** (exponents[i]+1) < 21:
        exponents[i] = exponents[i] + 1

for i in range(0, len(primes)):
    product = product * (primes[i] ** exponents[i])

print(product)
