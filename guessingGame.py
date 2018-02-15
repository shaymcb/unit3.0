#Shaylee McBride
#15Feb2018
#guessingGame.py - it's a guessing game

from random import randint

num = randint(1,100)

tries = 0
while 1==1:
    guess = int(input('Guess a number between 1 and 100: '))
    tries += 1
    if guess == num:
        print('You win! It took you',tries,'guesses.')
        break
    elif guess < num:
        print('too low')
    else:
        print('too high')
