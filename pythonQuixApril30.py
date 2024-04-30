# Quiz rules:

# This quiz is open book/ open note: you may use class notes, notes from the instructor github, w3schools.com as well as google to search for relevant articles
# You MAY NOT use chatgpt or any AI software for this quiz. Any usage of AI tools will result in an automatic failure.

# No phones are allowed during the quiz. Failure to put your phone away will result in an automatic failure.

# There is no talking during the quiz. 

# You will have the entire class period to complete the quiz. 

# To recieve full credit please show your work by providng clues, keywords, and notes you wrote down to solve
# the problem.  

# 1. What is a while loop, what is a for loop, and what is the difference between the two.
# Please write your response using complete sentences.

# While loop- A while loop is a python function that repeats a block of code as long as an condition is true.
# For loop- A for loop is a python operator that repeats a block of code usually a certain ammount of times or with a limit.
# the difference between the both is while loops doesnt usually use conditional statements for code, while for loops can/does. 

# 2. Name and describe three python operator families. Plese write your response using complete
# sentences.

# arithmatic- The arithmatic operator family contains anything with math, such as addition, subtraction, and more.
# comparison- The comparison family uses some logic, to compare two things or more in a block of code.
# Logic- The Logic operator allows the program to tell if something is true or isnt true, to be able to continue the code.

# 3. Create a function that will accept 3 arguements. 
# This function should multiply the first 2 arguments and then
# subtract the last argument from the sum of the first 2.

def Question_Three(Number1, Number2, Number3):
    print(Number1 *Number2 + Number3)
Question_Three(4, 5, 6)

# 4. Research the range() function. Then create a function that takes 2 arguements. 
# Your function should take the range of the first argument and multiply those numbers by the second 
# argument. 

def Question_Four(Number1, Number2):
    print(range(Number1))
    print(Number2 *0)
    print(0)
    print(0 *7)
Question_Four(7, 8)

# 5. Create a function that will ask the user guess the correct number.
# Your function should take a user input which will be their guess. Your function should 
# generate a random number between 1 and 5. If the user guesses the number correctly, the program
# will inform the user they guessed correctly and end the game. If the user guesses incorrectly, they
# will be informed their guess is incorrect and to guess again. The user should only be able to guess
# incorrectly 3 times. If they get the 3rd attempt wrong, the program should inform they user they have lost
# the game.

def Question_Four():
    RandNumb = [1,5]
    UserInput = input('Please enter your first guess:  ')

while UserInput != 


# 6. Create a function that will act as a saving calculator. Your function should take several inputs from
# the user. Your program should ask the user what they are saving up for, how much does it cost, and how much 
# they want to deposit this week. Your program should repeat asking the user how much would they like to
# save this week, until the goal amount has been satisfied. Each time the user makes a deposit, your
# program should inform them how many weeks they have left, how much money they have deposited, and how
# much money their is remaining to reach their goal.

def Question_6():
    MoneyGoal = 5000
    UserInput1 = input('What are you saving up for? :  ')
    UserInput2 = input('How much does it cost? :  ')
    UserInput3 = input('How much would you like to deposit this week? :  ')
while UserInput3 != MoneyGoal:
    print(MoneyGoal - UserInput3)
    UserInput3 = input('How much would you like to deposit this week? :  ')
Question_6()

# Ex. if my goal is to save $500, and deposit $20 dollars for that week, it should tell me that 
# It will take me 25 weeks to reach my goal based on the 20 dollar deposit, I have $20 saved,
# and that I need $480 more dollars.

# If I deposit $40 dollars the next week it should tell me
# it will take 10 weeks to reach my goal based on the $40 dollar deposit, I have $60 saved, and that I need 
# $440 more dollars to reach my goal.