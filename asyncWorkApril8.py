# Async Activity April 8th, 2024

# 1. In your own words, describe what a while loop is?

# Answer 1. A while loop means as long as a statement is true, The function will repeat until stopped, or disrupted.

#2. Create a function that uses a while loop to determine if a user has typed in 
# the the correct word guess. If the user types in the wrong word, your program 
# should inform them that their guess was inccorect and to try again, but if the
# user guesses the word correctly, your program shoul tell the user they have 
# guessed correctly and have won the game, stopping the loop.

def userWord_Guess():
    wordGuess = 'supercalifragilisticexpialidocious'
    userInput = input('What is your word guess ?  ')

    while userInput != wordGuess:
        print('Incorrect word guess, try again.   ')
        print('Wait five more seconds. ')
        print('4')
        print('3')
        print('2')
        print('1')
        userInput = input('Please re-enter your word guess.  ')
    if userInput == wordGuess:
        print('Correct word guess.')
        print('___________________')
        print('ending loop.')
userWord_Guess()