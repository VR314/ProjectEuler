import re
import decimal

"""
*	Problem #: 026
*	Date Attempted: 06/07/20
*	Date Solved: 06/07/20
*
*	Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
*
*	Answer: 983
"""

STRING = ""


def distill(x):
    sliceSize = 2
    while sliceSize < len(x):
        arr = []
        for i in range(0, 4):
            arr.append(x[i*sliceSize: i * sliceSize + sliceSize])
        for i in range(0, len(arr) - 1):
            if arr[i] != arr[i+1]:
                sliceSize += 1
                break
        else:
            return x[:sliceSize]
    return ""


def lenRepeats(denom):
    with decimal.localcontext() as ctx:
        ctx.prec = 10000
        STRING = str(decimal.Decimal(1)/decimal.Decimal(denom))[2:]

    pattern = re.compile(r'(\d+)\1+')
    matches = pattern.finditer(STRING)

    for match in matches:
        STRING = match.group(0)
        break

    return len(distill(STRING))


denoms = range(1, 1000)
lens = []
for i in range(1, 1000):
    lens.append(lenRepeats(i))

print(denoms[lens.index(max(lens))])
