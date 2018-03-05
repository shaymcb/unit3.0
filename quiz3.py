#Shaylee McBride
#5Mar2018
#quiz3.py

n = -15
while n <= -9:
    print(n)
    n += 1

for i in range(9):
    print(50 - 4*i)

total = 0
for i in range(-100,1000+1,2):
    total += i
print(total)

while True:
    text = input('Enter text: ')
    if 'alpaca' in text:
        break