def entrancePasscode(UserCode):
    actualPassCode = 'get_this_money'
    UserCode = input('Please enter user code. ')
    if UserCode == actualPassCode:
        print('Password correct. You may enter')
    else: 
        print('Password is incorrect. You may not enter')
entrancePasscode('get_this_money')