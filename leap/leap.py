def leap_year(year):
   # year is a leap year if:
   # is divisible by 4
   # is not divisible by 100
   # is divisible by 400
   return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
