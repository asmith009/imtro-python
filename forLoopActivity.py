# While Loop - repeats a block of code instructions, so long a condition is true.

#i = 0 # i - stands for iterator, its the strating point for a while loop.
#
#while i == 0:
#    print(i)
## the result here is that i (or zero) will continue to print for ever because the condition is true.

# For Loops - repeats a block of code instructions, up to the number of items in a group.

def ddg_Game():
    groupOfKids = ['duck', 'duck', 'duck', 'goose', 'duck', 'duck']
    for kid in groupOfKids:
    # for every item in this list;
    # kid is the item groupOfKids is the list.
        if kid == 'goose':
            print('Found the goose. ')
            continue
        print(kid)
        # print each item; print each kid.

#ddg_Game()

def rpgGame():
    userWeapon = input('What weapon would you like to use?  ')
    print(inventory)
    inventory =['sword','gun','shelid','potion','grenade']
    for item in inventory:
        if item == userWeapon:
            print(f'you have equipped the {userWeapon} to your fighter.  ')
        print('here is you current inventory')
rpgGame()
