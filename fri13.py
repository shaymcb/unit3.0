#Shaylee McBride
#15Feb2018
#fri13.py

from calendar import weekday
from datetime import date

year = date.today().year
month = date.today().month
dates = 0

while dates <= 10:
    weekday = weekday(year,month,13)
    if weekday == 5:
        print(month+'/13/'+year)
        dates += 1
    month += 1
    if month == 13:
        year += 1
        month = 1
