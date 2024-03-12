# Intro to Python Async Work
# Monday March 11th, 2024.

# INSTRUCTIONS
# Create a new python file called async_3_11.py
# Answer the following questions. Once you've completed the questions, commit
# and sync your work.
# This activity must be completed by the end of class in order to recieve
# a grade.

# REMEMBER - TAKE YOUR TIME AND DO YOUR BEST! DO NOT GIVE UP! 

# 1. Which Python datacasting function would
# you use if you wanted to convert a string data type
# into an integer data type? Please write your response
# in a complete sentence. 

# Answer.1- The Python datacasting function i would use to convert a string(str), into and intger(int)
#           would be int()
# Example:
#           int(input('This is how i would use it'))

# 2. Create a list called numbCol that contains three (3 ) colors and three (3) numbers.

# Answer.2-
numbCol = ['blue' , 'red' , 'orange' , '12' , '13' , '14']

# 3. You have been hired by a University to create
# a scholarship function. The client would like to provide 
# students a scholarship to their school based on the following
# conditions; 
# - If the user has never gotten a loan before and,
#-  if the user has never been to college before.
# The client would like you to use the logical NOT operator that will
# compare the condtions and return false. If the result is false, the client
# would also like the program to print the message "congrats! you've gotten the scholarship."
# the client has given you the choice on how to enter data for your function.
# you may enter data using input or pass in data into your function as parameters. 

def scholarShip(UserScholarship):
    if UserScholarship == 'Yes':
        print('You are unable to get a Scholarship.')
    elif UserScholarship == 'No':
        print('Congrats! Youve gotten the scholarship.')
scholarShip('No')

# Amari.A.Smith