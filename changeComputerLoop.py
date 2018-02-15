#Shaylee McBride
#15Feb2018
#changeComputerLoop.py

money = int(input('Enter the number of cents you need in change: '))
quarters = 0
dimes = 0
nickels = 0
pennies = 0

while money > 0:
    if money >= 25:
        quarters += 1
        money -= 25
    elif money >= 10:
        dimes += 1
        money -= 10
    elif money >= 5:
        nickels += 1
        money -= 5
    else:
        pennies = money
        money = 0

print('Quarters:',quarters)
print('Dimes:',dimes)
print('Nickels:',nickels)
print('Pennies:',pennies)
