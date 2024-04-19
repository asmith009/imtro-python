# Warm up Tuesday April 16th, 2024.

import random

# 1. In your own words, explain the difference between an Python For Loop and a
# Python While Loop.

# Answer 1. A python while loops continues on for ever unless stoped or disrupted, and a for loop is given an ammount of times the program shoukd loop.

# 2. Create a loop that will iterate over a list of numbers. For evey number in your loop,
# it should multiply that number by 3.
def Numbers():
    NumbersList = [1, 2, 3, 4, 5, 6, 7, 8]

    for Number in NumbersList:
        print(Number * 3)


# 3. Use the following code snippet below to create a guessing game function. 
# The code below will generate a random number for you. You must write a loop that will
# ask the user to input their guess, if they guess incorrectly, the program will repeat 
# itself and ask the user to guess again. The program should continue to ask them to
# guess until they've gotten it correctly. Once they guess the correct number the program
# will congratulate them and the loop will stop. 

# generates a random number between 1 and 10
randomNumber = random.randint(1, 10)
print(f'Random number is now: {randomNumber}')
userInput = int(input('enter your guess.  '))
while userInput != randomNumber:
    print('Incorrect guess, try again.  ')
    userInput = int(input('re-enter your guess.  '))
    if userInput == randomNumber:
        print('You have guessed correctly.  ')
        print('ending the loop')