#Shaylee McBride
#15Feb2018
#baseConverter.py

base10 = int(input('Enter a base-10 number:' ))
original = base10
base = int(input('What base would you like to convert to? '))

#find highest place
division = 1
places = 0
while division < base10:
    division = division * base
    places += 1
division = division / base

#loop to find place values
num = ""
while base10 > 1:
    place = base10//division
    base10 = int(base10 - place*division)
    if place > 9:
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #accomodate for double-digits
        place = s[place-10]
    else:
        place = str(place)
    num = num+place
    division = division / base
    places -= 1

#account for zeros
num = num+"0"*places
print(original,'in base',base,'is',num)
