"""Write a program that reads a date from the user and computes its immediate successor. For example, if the user enters
 values that represent 2013-11-18 then your program should display a message indicating that the day immediately after
 2013-11-18 is 2013-11-19. If the user enters values that represent 2013-11-30 then the program should indicate
 that the next day is 2013-12-01. If the user enters values that represent 2013-12-31 then the program should indicate
 that the next day is 2014-01-01. The date will be entered in numeric form with three separate input statements;
  one for the year, one for the month, and one for the day. Ensure that your program works correctly for leap years."""


day = int(input('Day: '))
month = input('Month: ').lower()
year = int(input('Year: '))
next_day = None
next_month = None
next_year = year
isLeapYear = None

# check if the year is leap
if year % 400 == 0:
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False

# process special cases for the last day of each month, including February in leap and not ordinary years
if day == 31 and month == 'january':
    next_day = 1
    next_month = 'february'
elif day == 28 and month == 'february':
    if isLeapYear:
        next_day = day + 1
        next_month = month
    else:
        next_day = 1
        next_month = 'march'
elif day == 29 and month == 'february':
    next_day = 1
    next_month = 'march'
elif day == 31 and month == 'march':
    next_day = 1
    next_month = 'april'
elif day == 30 and month == 'april':
    next_day = 1
    next_month = 'may'
elif day == 31 and month == 'may':
    next_day = 1
    next_month = 'june'
elif day == 30 and month == 'june':
    next_day = 1
    next_month = 'july'
elif day == 31 and month == 'july':
    next_day = 1
    next_month = 'august'
elif day == 31 and month == 'august':
    next_day = 1
    next_month = 'september'
elif day == 30 and month == 'september':
    next_day = 1
    next_month = 'october'
elif day == 31 and month == 'october':
    next_day = 1
    next_month = 'november'
elif day == 30 and month == 'november':
    next_day = 1
    next_month = 'december'
elif day == 31 and month == 'december':
    next_day = 1
    next_month = 'january'
    next_year = year + 1
else:
    next_day = day + 1
    next_month = month
    next_year = year

print(f'The next day is {next_day} {next_month.capitalize()} {next_year}.')
