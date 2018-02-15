#Shaylee McBride
#15Feb2018
#gauss.py - adds up numbers

num1 = int(input('Enter lower bound: '))
num2 = int(input('Enter upper bound: '))
step = int(input('Enter step: '))

total = 0
for i in range(num1,num2+1,step):
    total += i
print(total)
