
"""
*	Problem #: 017
*	Date Attempted: 06/02/20
*	Date Solved: 06/02/20
*
*	If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
*   how many letters would be used?
*
*	Answer: 21124 
"""

d = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


def wordLength(x):
    s = ''
    if x == 1000:
        s = s + d[int(x/1000)] + " " + d[1000]
        s = s.replace(' ', '')
        print(s)
        return len(s)
    if x >= 100:
        s = s + d[int(x/100)] + " " + d[100]

    if x % 100 != 0:
        if x > 100:
            s = s + " and "
        if x % 100 > 20:
            s = s + d[x % 100 - x % 10] + d[x % 10]
        else:
            s = s + d[x % 100]

    s = s.replace(' ', '')
    print(s + ": " + str(len(s)))
    return len(s)


sum = 0
for i in range(1, 1001):
    sum = sum + wordLength(i)

print(sum)
