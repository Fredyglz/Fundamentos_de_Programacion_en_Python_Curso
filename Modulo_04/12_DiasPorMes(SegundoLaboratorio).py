﻿def isYearLeap(year):
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
    

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")