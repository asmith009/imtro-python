# 1.What are the two parts needed to create a function. Describe what they do.
# part 1. Is to define the function. Called function defenition.
# part 2. Is to call the function, so the program knows when to operate that function, called function call.
#         saves the function and executes the function(s) when called.

# 2. Explain the differnece between function parameter and function argument.
# Answer 1: Function parameter is the variables listed in a function defenition.
# Answer 2: Function arguement is the values in a function.

# 3.

def userName_AndAge(UserName, UserAge): 
    UserAge = UserAge + 10
    UserName = input('What is you name?')
    print(f'good morning {UserName} you will be {UserAge} in 10 years')

userName_AndAge('Amari',14)

def passWordCheck(userPassword):
    password = '123'
    if userPassword  == password:
        print("password correct. Welcome to the site")
    else:
        print('password incorrect. Please try again.')

passWordCheck('1323')
