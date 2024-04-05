# Answer 1. As long as the condition is correct repeat until stopped inside the block of code.
# Answer 2. An iterator inside of a python loop is the starting point telling the program what to repeat(or loop).
# Answer 3.
# I would add a variable for ammount of times the msg is repeated.
# then i would write in my block of code, While AmmountOfMsgs < 5, then print the ammount of times you can write this msg ran out.

# variable being assigned string w/ the value of hello.
#def message():
#    msg = 'hello'
#    while msg == 'hello':
# while >> so long as this is true.
# variable msg is the same as hello (hello is the same as hello)
#        print(msg) # print this out so long as the statement above is true
#        msg = input('type a new message: ')
#        if msg == 'goodbye':
#         print('ending loop. ')
#message()


# Create a function that will ask the user to enter a date to check if it is user's birthday. the function should have the correct birth datv stored
# as a variable. The user should have been prompted to enter the month and date. if the day they entered is incorrect, print a message informing them
# it is incorrect an re-ask them to enter the correct birthday. If the user enters the correct birth date, your function should congratulate them and
# stop the loop

#def checkBirthday():
#    month = [1,2,3,4,5,6,7,8,9,10,11,12]
#    day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
 #   
  #  UsersBirthday = [month[1],day[1]]
   # print(UsersBirthday)
    #userInput =''
    #
  #  w#hile userInput != UsersBirthday:
      #  userInput_Month = ('Please enter the correct birthday (Month)  ')
       # userInput_day = ('Please enter the correct birthday (Day)  ')
        #
 #       i#f userInput_Month == UsersBirthday:
          #  print('congrats! happy birthday.  ')
#checkBirthday()















def numberIncrement():
    i = 0 # iterator = starting point for our loop.

# ketyword, all while means is so long as thuis condition is true.
    while i < 3:
        print('Welcome to python.  ') # print this on a loop 3x.
        i += 5
        print(f'i is now {i}')

dailyMsg = input('Please neter if it is morning or afternoon?   ')

while dailyMsg == 'morning':
    print('Good Morning.  ')
    print('waiting...3 - reading code line for line  ')
    print('waiting...2 - reading code line for line  ')
    print('waiting...1 - reading code line for line  ')
    dailyMsg = input('Please enter what time of day it is now:   ')
if dailyMsg == 'afternoon':
        print('Good afternoon  ')
        print("__________________")
        print('ending loop  ')



    
UserInput = input('Please enter your passcode.  ')

while UserInput != '12345':
    print('Password is incorrect')
    print('Wait five more seconds. ')
    print('4')
    print('3')
    print('2')
    print('1')
    UserInput = input('Please enter your password.  ')
if UserInput == '12345':
     print('Correct password, welcome.  ')