# Async Assignment March 3rd, 2024. 

# Complete and solve the following prompts.
# Make sure to write down the clues and keywords you found.
# (Make sure to include your clues and keywords to recieve full credit)

# Commit and sync your work before the end of class. 
# This will count toward your class activity grade. 

# Prompt #1- Elevator Conditional Function Execercise.

#keywords
#functions- instructions that only run when called.
#Input()- lets your program accept data from the user.
#string data ype-
#variables-
#conditionals (iflelse/elif)- allows us to run specific instructions based on
#specific conditions.
#elevator should take in floor number and send user to that floor.

def ElevatorSystem():
    UsersFloor = input('What floor would you like to go to? Choose the number/letter of the floor.')
    if UsersFloor == 'M':
        print('Taking you to the lobby.')
    elif UsersFloor == 'B':
        print('Taking you to the basement.')
    elif UsersFloor == 'R':
        print('taking you to the roogtop. Be careful.')
    elif UsersFloor == '1':
        print('Taking you to the gym.')
    elif UsersFloor == '2':
        print('Taking you to the resturaunt.')
    elif UsersFloor == '3':
        print('Taking you to the workspace.')
    elif UsersFloor == '4':
        print ('taking you to the living quarters.')
    else:
        print('This floor is unavailabe, or does not exist. PLease try again.')

ElevatorSystem()

# You have been hired by a architeture firm to assist 
# with developing their elevator system. They have asked 
# you to develop a function that will accept a user's input. 
# your program should ask the user to enter a floor number. 
# When an user enters a number they will be sent to a specific 
# floor in the building. If the user enters a floor number that does not
# exist, your program should inform the user that the floor they entered
# does not exist and to enter another number and to try agin.

# The architects have given you the following 
# lists of floors for their building:

# M = 'lobby'
# B = 'basement'
# R = 'rooftop'
# 1 = 'gym'
# 2 = 'restuarant'
# 3 = 'workspace'
# 4 = 'living quarters'

#___________________________________________________________

# Prompt #2- Amusement Park Conditional Function
# You have been hired by an amusement park to develop a function
# that allows users to access their roller coasters by entering their age
# and height. Your program should take the user's height and age as parameters.
# Your client has very specific requirements for thier guests 
# to ride their roller coasters and have provided you with the following 
# conditions that they would like your program to check for. 

# user must be atleast 5.2 or taller and atleast 14 years old or older 
# in order to ride roller coaster 1. 

# if the user is shorter than 5.2 but at least 14 years of age or older,
# they can ride the roller coaster 2.

# if the user is shorter than 5.2 and also younger than 14 years of age,
# they can ride roller coaster 3. 

# if the user enters information incorrectly, give them an error message
# and tell them that they entered their information incorrectly. 

#keywords
#check for height.
#.comparison operatorsless, greateter than- check for age and height.
#we need to write a function.
#we need parameters - height and age.

def RollerCoaster(Height, age):
    if Height <= 5.1 and age <= 14:
        print('you are able to ride roller coaster number 3.')
    elif Height <= 5.2 and age >= 14:
        print('you are able to ride roller coaster number 2')
    elif Height >= 5.2 and age >= 14:
        print('you are able to ride roller coaster number 1')
    else:
        print('If your info does not make you eligible to ride any of the roller coaters there could be an error please ask a local employee for assistance. ')
 
RollerCoaster(5.5, 14)