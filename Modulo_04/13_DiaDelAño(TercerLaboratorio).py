
def isYearLeap(year):
    if (year % 100 != 0) and (year % 4 == 0):
        return True
    elif (year % 400 == 0):
        return True
    return False

def daysInMonth(year, month):
    daysMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    bisiesto = isYearLeap(year)
    if bisiesto and month == 2:
        return daysMonths[month - 1] + 1
    return daysMonths[month - 1]

def dayOfYear(year, month, day):
    days = 0
    for i in range(month - 1):
        days += daysInMonth(year, i+1)
    return days + day

print(dayOfYear(2020, 10, 10))