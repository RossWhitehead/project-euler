#    1 Jan 1900 was a Monday.
#    Thirty days has September, April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import calendar

def execute():
  print("Executing problem 19...")

  count = 0

  startMonth = 1
  startYear = 1901
  endMonth = 12
  endYear = 2000

  for year in range(startYear, endYear + 1):
    for month in range(startMonth, endMonth + 1):
      count += calendar.weekday(year, month, 1) == 6

  print(count)

execute()