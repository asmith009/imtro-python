i = 0 # variable being assigned the value a zero
# i = iterator. Our loop starting point.

while i <= 10: # so long as 0 is less than 5...
    print(i) # print the variable
    i += 2 # adding 1 to our variable

# while = so long as a condition is true, do this...
def airMaxInventorySystem():
airMax = 5 # our iterator/ starting

while airMax > 0:
    usercart = input('would you like to buy these sneakers')
    if usercart == 'y':
        airMax -=1
        print(f'air max inventory : {airMax}')
    if airMax == 0:
        print('we are out of stock.')

def JapanSavings():
    japan_Trip_Savings_Account = 0
    while japan_Trip_Savings_Account <= 10000:
        user_Deposit = int(input('How much would you like to put away for your trip.'))
        japan_Trip_Savings_Account += user_Deposit
        print(f'you have {japan_Trip_Savings_Account} In your account. ')
    print('congrats, your on your way to Japan. ')

JapanSavings()
