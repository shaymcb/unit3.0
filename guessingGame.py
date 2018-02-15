#Shaylee McBride
#15Feb2018
#guessingGame.py - it's a guessing game

from random import randint

num = randint(1,100)

while 1==1:
    guess = int(input('Guess a number between 1 and 100: ')
    if guess == num:
        print('You win!')
        break
    elif guess < num:
        print('too low')
    else:
        print('too high')
