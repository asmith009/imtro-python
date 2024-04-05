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