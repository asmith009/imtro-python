# Midterm quiz. Amari Smith
# Create a new python document called midtermquiz.py
# Complete the following questions.
# Once you have comepleted your quiz, commit and sync your work to your GitHub. 

#RULES
# This quiz is open book; you may use your notes, google (only if you are viewing arcticles about python), W3schools only. Any other website
# is prohibitied.
# No phones are allowed during the quiz. refusal to put away a phone will result in failure.
# There is no talking during the quiz. If you complete the quiz, notify the instructor that you
# have finished. Once that is done, you are free to use your device and browse the web quitely. 

# Good Luck Amari Smith

# 1. In your own words, describe what the difference
# between a function arguement and a function parameter.
# Write your response using complete sentences.

# Answer . To me the differnece between a function argument and a function parameter is, a function parameter is used as a place holder for the variable.
#           An function argument is given to the computer as kind of like and input, to tell the computer what to print.

# 2. In your own words, describe what each of the following errors means.
# Write your response using complete sentences.

# syntax error - As syntax error is an error given from the computer to you because of missing indenttions, or using the wrong synbols that the program cant read
# type error - A type error is pretty self explanatory, you may spell a function worng, or use a operator in the wrong place in a black of code.
# name error - A name error is when something in your block of code/program is not defined.

# 3. What function would I use if I wanted to convert an integer data type into 
# a string data type?

# Answer . The function i would use to change an integer data type into a string is the function str/string.

# 4. What function would I use if I wanted to change a float data type into a 
# an integer data type?

# Answer . The function i would use for this is the int/integer function.

# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 

# 1. You cant name something starting with a digit.
# 2. The name must start with a letter.
# 3. Use a name to describe the value.

# 6. Name the operator family each of these symbols are a part of 
# and describe how each of these sybmols are used. Write your response
# useing complete sentences. 

#symbols
# = - this operator is called assignment, this assigns a job/duty to the computer/program
# == - This ioperator is called comparison, Comparison compares two or more values in a program.
# =! - This operator is called the true or false operator, This determines if one thing is true or false in a program.

# 7. You have been hired as an engineer to develop a car speed detection system.
# the car company would like to create a function where if the user goes over a certain
# speed it will notify them to change gears. The client has provided you with the following
# guidelines on how they would like the gear system to work:
# if the driver is going over 20mph, alert the driver to shift to gear 1
# if the the driver is going over 30mph, alert the driver to shift to gear 2
# if the driver is going over 40mph, alert the driver to shift to gear 3
# if the driver is going over 70mph, alert the driver to shift back to gear 1.
# the client would like you to pass in the speed that the user is going as an argument. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

#Clues
# Goes Over - This told me to use greater than and equal to
# If - This told me i needed to use conditional statements
# pass in the speed as an argument - this told me that i didnt need to use input

def Speeddetection(UserSpeed):
    if UserSpeed >= '21':
        print('Shift to gear one please')
    elif UserSpeed >= '31':
        print('Shift to gear two please')
    elif UserSpeed >= '41':
        print('Shift to gear three please')
    elif UserSpeed >= '71':
        print('Shift back to gear one please')

Speeddetection('96')

# 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# 2 arguments - this told me i didnt need input
# either - This told me i needed to use conditional statements
# time of the day, and day of the week -  this told me the conditionals i needed for the program

def FitnessmealPlan(DayOfTheWeek, TimeOfTheDay):
    if DayOfTheWeek == 'monday' and TimeOfTheDay == 'morning':
        print('2 eggs and a apple')
    elif DayOfTheWeek == 'monday' and TimeOfTheDay == 'afternoon':
        print('bbg grilled chicken and broccoli')
    elif DayOfTheWeek == 'tuesday' and TimeOfTheDay == 'morning':
        print('oatmeal with strawberries and blueberries')
    elif DayOfTheWeek == 'tuesday' and TimeOfTheDay == 'afternoon':
        print('baked chicken with kale')
    elif DayOfTheWeek == 'wednesday' and TimeOfTheDay == 'morning':
        print('fruit salad')
    elif DayOfTheWeek == 'wednesday' and TimeOfTheDay == 'afternoon':
        print('curry goat with rice and cabbage')
    elif DayOfTheWeek == 'thursday' and TimeOfTheDay == 'morning':
        print('pankcakes and turkey sausage')
    elif DayOfTheWeek == 'thursday' and TimeOfTheDay == 'afternoon':
        print('eggplant pasta')
    elif DayOfTheWeek == 'friday' and TimeOfTheDay == 'morning':
        print('steak and eggs')
    elif DayOfTheWeek == 'friday' and TimeOfTheDay == 'afternoon':
        print('cheeseburger and fries')
    elif DayOfTheWeek == 'saturday' and TimeOfTheDay == 'morning':
        print('oatmeal')
    elif DayOfTheWeek == 'saturday' and TimeOfTheDay == 'afternoon':
        print('baked chicken with string beans')
    elif DayOfTheWeek == 'sunday' and TimeOfTheDay == 'morning':
        print('oatmeal')
    elif DayOfTheWeek == 'sunday' and TimeOfTheDay == 'afternoon':
        print('steak and spinach')
FitnessmealPlan('wednesday', 'afternoon')
    

# monday morning= 2 eggs and an apple
# monday afternoon= bbq grilled chicken and broccoli

# tuesday morning= oatmeal with strawberries and blueberries
# tuesday afternoon= baked chicken with kale

# wednesday morning= fruit salad
# wednesday afternoon= curry goat with rice and cabbage

# thursday morning= pancakes and turkey sausage
# thursday afternoon= eggplant pasta

# friday morning= steak and eggs
# friday afternoon= cheesburger and fries

# saturday morning= oatmeal
# saturday night= baked chicken with string beans

# sunday morning = oatmeal
# sunday night = steak and spinach

# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

# if- this told me i was using conditional staements
# above/below 85% - this told me i was using < or >
# argument(s) - this told i didnt need input function

def Academic_Honors(StudentOverAllGrade, StudentSATScore):
    if StudentOverAllGrade > 85 and StudentSATScore == 'passed':
        print('You have acheived the academic honors list!!')
    elif StudentOverAllGrade < 85 and StudentSATScore == 'passed':
        print('Congratulations for passing the SAT, but you did not make the academic honors list.')
    elif StudentOverAllGrade > 85 and StudentSATScore == 'failed':
        print('Congratulation on you overall grade, but you did not make the list')
    elif StudentOverAllGrade < 85 and StudentSATScore == 'failed':
        print('continue studying and try again next semester.')

Academic_Honors(100, 'passed')

# 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.

def OutsideTemperature():
    UserInput = input('how many degrees is it outside?  ')
    if UserInput > 60:
        print('It is warm outside')
    if UserInput > 80:
        print('It is hot outside')
    if UserInput < 50:
        print('It is cold outside')
    if UserInput > 50:
        print('It is not warm outside, but its not too cold.')
OutsideTemperature()


# Amari Smith