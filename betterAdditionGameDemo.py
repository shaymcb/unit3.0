#Shaylee McBride
#28Feb2018
#betterAdditionGameDemo.py - more loop practice

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    answer = int(input('what is '+str(num1)+' + '+str(num2)+'?'))
    
