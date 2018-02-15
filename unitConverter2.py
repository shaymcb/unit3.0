#Shaylee McBride
#29Jan2018
#unitConverter.py - converts things

print('1) kilometers to miles')
print('2) kilograms to pounds')
print('3) liters to gallons')
print('4) Celsius to Fahrenheit')
print(' ')
choice = int(input('Choose a number: '))

if choice == 1:
    km = float(input('Enter a distance in kilometers: '))
    print(km,'kilometers is',0.621*km,"miles")
elif choice == 2:
    kg = float(input('Enter a weight in kilograms: '))
    print(kg,'kilograms is',2.205*kg,'pounds')
elif choice == 3:
    L = float(input('Enter an amount in liters: '))
    print(L,'liters is',0.264*L,'gallons')
elif choice == 4:
    c = float(input('Enter degrees Celcius: '))
    print(c,'degrees Celcius is',9/5*c+32,'degrees Fahrenheit')
else:
    print('you done fucked up-- try again.')

