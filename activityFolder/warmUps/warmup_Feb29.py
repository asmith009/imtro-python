# 1. In my own wards what a conditional statements are is functions inside of python that prctically gives options.

# 2.

def check_highScore():
    UserScore = int(input('what is your current score? '))
    if UserScore > 3000:
        print('High Score reached, Good Job!')
    else:
        print('Sorry high score not reached, keep trying.')

check_highScore()


month = int(input("what month is it?"))
season = [1,2,3,4,5,6,7,8,9,10,11,12]

if month > season[10]:
    print("the season is winter.")
elif month > season[2] and month < season[5]:
    print("the season is spring.")
elif month > season [5] and month < season[8]:
    print("the season is summer")
elif month > season[8] and month < season[12]:
    print("the season is fall.")
else:
    print("something went wrong. check your code.")