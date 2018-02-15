#Shaylee McBride
#15Feb2018
#baseConverter.py

base10 = int(input('Enter a base-10 number:' ))
base = int(input('What base would you like to convert to? '))


#find highest place
division = 1
places = 0
while division < base10:
    division = division * base
    places += 1
division = division / base
places -= 1

num = ""
while base10 > 1:
    place = base10//division
    base10 -= place*division
    if place <= 9:
        place = str(place)
    else:
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        place = s[place-9]
    num = num+place
    division = division / base

print(num)