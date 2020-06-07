
"""
*	Problem #: 019
*	Date Attempted: 06/06/20
*	Date Solved: 06/06/20
*
*	How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
*
*	Answer: 21124 
"""

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def february(year):
    if year % 4 != 0:
        return 28
    else:
        if year % 100 != 0:
            return 29
        elif year % 400 == 0:
            return 29
        else:
            return 28


first = 2  # sunday = 0
month = 1
year = 1901
count = 0
print(str(month) + " 1st " + str(year) + " was a " + str(first))
while year < 2001:
    if month == 2:
        days = february(year)
        first = (days + first) % 7
        month = month + 1
    elif month == 12:
        year = year + 1
        first = (months[month] + first) % 7
        month = 1
    else:
        first = (months[month] + first) % 7
        month = month + 1

    print(str(month) + " 1st " + str(year) + " was a " + str(first))
    if first == 0:
        count = count + 1

print(count)
