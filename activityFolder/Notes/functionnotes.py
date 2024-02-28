# functions - a set instructions that execute one task in a program.

#functions have 2 parts:
# 1. function defenition - the instruction on how the function works for the program.

def goodAfternoon():
    print('good afternoon team!')

# 2. function call - tells the program to run/execute our function instructions.
goodAfternoon()

#function parameters and Arguments - external data
#passed uinto a function
#data type = strings, floats, boolean, etc. data base

def giftCard_add5(user_GiftCard):
    newBalance = user_GiftCard +5
    print(f'your new gift card balance is {newBalance} dollars.')

giftCard_add5(200)

def giftCard_Add10(user_Giftcard):
    newBalance = user_Giftcard + 10
    print(f'your new gift card balance is {newBalance} dollars.')

giftCard_Add10(1200)

() # ROUND brackets are for functions
[] #SQUARE brackets are for lists
{} #CURLY brackets are data, but can also be objects
# (objects are just a collection pf data.)

def salary_140k():
    print('here are 140k jobs...')
def salary_120k():
    #write some instructions...
    print('here are 120k jobs...')

def jobSearch_bySalary(desiredSalary):
    print('show these results thata re in this range')
    print(f'here are jobs that pay {desiredSalary}')
    salary_120k()
    salary_140K()
    slary_200k()

jobSearch_bySalary(120000)