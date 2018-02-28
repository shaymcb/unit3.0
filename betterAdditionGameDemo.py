#Shaylee McBride
#28Feb2018
#betterAdditionGameDemo.py - more loop practice

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-5000,5000)
    num2 = randint(-5000,5000)
    answer = int(input('what is '+str(num1)+' + '+str(num2)+'? '))
    if answer == num1+num2:
        numCorrect += 1
    else:
        print('WRONG!')
        print('The answer was',num1+num2)
print('You win!')