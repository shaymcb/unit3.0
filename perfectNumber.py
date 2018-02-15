#Shaylee McBride
#15Feb2018
#perfectNumber.py

num = int(input('Enter a number: '))

i = 1
total = 0
while i < num:
    if num%i == 0:
        total += i
    i += 1

if total == num:
    print('Perfect')
else:
    print('Not Perfect')
