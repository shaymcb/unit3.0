#Shaylee McBride
#15Feb2018
#fri13.py

from calendar import weekday
from datetime import date

year = date.today().year
if date.today().day <= 13:
    month = date.today().month
else:
    month = date.today().month + 1
    if month == 13:
        month = 1
        year += 1
dates = 0

while dates <= 10:
    day = weekday(year,month,13)
    if day == 4:
        print(month,'/ 13 /',year)
        dates += 1
    month += 1
    if month == 13:
        year += 1
        month = 1
