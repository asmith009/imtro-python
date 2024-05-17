# The program idea is to making a shopping  app. This apps sells clothes and shoes at a affordable price.Our program will allow more users to enter our app by giving discounts based 
# on times, and dates. Such as Christmas. There will be a discount for christmas time for all users.
# your program trying to solve: Many consumers  want to own luxury items but may be discouraged  by high prices. 
# A shopping app offering discounted luxury goods makes these products more accessible to a wider audience, including students or young professionals on a budget.
# Who is your program designed for: this is designed for teenager and people who dont have money. The porgram is designed  for people who want to get high fashion clothes on a budget.


def HotMess():
    UserInput = input('Login or Signup: ')
    HomePage = ['HamburgerIcon', 'Pants', 'Shorts', 'Shirts', 'Sweaters', 'Coats', 'Jackets'  ]
    UsersCart = []
    MensPants = ['Baggy', 'Cargo', 'Kakis','BackToHomePage']
    MensShorts = ['Baggy', 'Cargo', 'Kaki']
    WomensPants = ['Leggings', 'SweatPants', 'HighwaistedJeans','BackToHomePage']
    WomensShorts = ['Compression', 'Gym', 'Jean','BackToHomePage']
    KidsPants = ['Sweat', 'Cargo', 'Jeans','BackToHomePage']
    KidsShorts = ['Gym', 'Cargo', 'Jean','BackToHomePage']
    Shirts = ['Graphic', 'Plain','BackToHomePage']
    Sweaters = ['Graphic', 'Plain', 'Hoodless','BackToHomePage']
    Coats = ['Puffer', 'Hoodless', 'Regular','BackToHomePage']
    if UserInput == 'Login':
        UserInput = input('Email: ')
        UserInput = input('Password: ')
        print(HomePage)
        UserInput = input('What would you like to use: ')
        if UserInput == 'HamburgerIcon':
            UserInput = input('Cart, Profile, Settings:  ')
            if UserInput == 'Cart':
                print(UsersCart)
                UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Profile':
                UserInput = input('Your Orders, Discounts, Coupons: ')
                if UserInput == 'Your Orders':
                    print('You havent orederd anything yet.')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Discounts':
                    print('There are no discounts available at this time.')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Coupons':
                    print('You have no coupons right now.')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Pants':
            print('These are our Pants options. ')
            UserInput = input('Mens, Womens, Kids:  ')
            if UserInput == 'Mens':
                print(MensPants)
                UserInput = input('What pair of pants would you like to add to your cart:  ')
                if UserInput == 'BaggyJeans':
                    print('You have added a pair of baggy jeans to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Cargo':
                    print('You have added a pair of Cargo pants to your cart.   ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Kakis':
                    print('You have added a pair of kakis to your cart')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Womens':
                print(WomensPants)
                UserInput = input('What pair of pants would you like to add to your cart:  ')
                if UserInput == 'Leggings':
                    print('You have added a pair of leggings to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'SweatPants':
                    print('You have added a pair of sweatpants to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'HighwaistedJeans':
                    print('You have added a pair of Highwaisted jeans to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Kids':
                print(KidsPants)
                UserInput = input('What pair of pants would you like to add to your cart:  ')
                if UserInput == 'Sweat':
                    print('You have added a pair of sweatpants to your cart')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Cargo':
                    print('You have added a pair of cargo oants to tour cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Jeans':
                    print('You have added a pair of Jeans to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Shorts':
            print('These are our Shorts options.')
            UserInput = input('Mens, Womens, Kids:  ')
            if UserInput == 'Mens':
                print(MensShorts)
                UserInput = input('What pair of shorts would you like to add to your cart:  ')
                if UserInput == 'Baggy':
                    print('You have added a pair of Baggy shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Cargo':
                    print('Your have added a pair of CargoShorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Kaki':
                    print('You have added a pair of kakiShorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Womens':
                print(WomensShorts)
                UserInput = input('What pair of shorts would you like to add to your cart:  ')
                if UserInput == 'Compression':
                    print('You have added a pair of Compression shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Gym':
                    print('You have added a pair of Gym shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == "Jean":
                    print('You have added a pair of Jean Shorts to your cart. ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Kids':
                print(KidsShorts)
                UserInput = input('What pair of shorts would you like to add to your cart:  ')
                if UserInput == 'Gym':
                    print('You have added a pair of Gym shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Cargo':
                    print('You h ave added a pair of cargo shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Jean':
                    print('You have added a pair of Jean Shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Shirts':
            print(Shirts)
            UserInput = input('What kind of shirts would you like to see:  ')
            if UserInput == 'Graphic':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white graphic shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black graphic shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey graphic shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Plain':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white plain shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black plain shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey plain shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Sweaters':
            print(Sweaters)
            UserInput = input('What kind of sweaters would you like to see:  ')
            if UserInput == 'Graphic':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white graphic sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black graphic sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey graphic sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Plain':
                UserInput = input('Choose a color. White, Black, grey:  ')
                if UserInput == 'White':
                    print('You have added a white plain sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black plain sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey plain sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Hoodless':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white hoodless sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black hoodless sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey hoodless sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Coats':
            print(Coats)
            UserInput = input('What kind of coats would you like to see:  ')
            if UserInput == 'Puffer':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white puffer coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black puffer coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey puffer coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Hoodless':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white hoodless coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black hoodless coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey hoodless coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Regular':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)


                

    
    
    elif UserInput == 'Signup':
        UserInput = input('First Name: ')
        UserInput = input('Last Name: ')
        UserInput = input('Email: ')
        UserInput = input('Password: ')
        UserInput = input('Username: ')
        print(HomePage)
        UserInput = input('What would you like to use: ')
        if UserInput == 'HamburgerIcon':
            UserInput = input('Cart, Profile, Settings:  ')
            if UserInput == 'Cart':
                print(UsersCart)
                UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Profile':
                UserInput = input('Your Orders, Discounts, Coupons: ')
                if UserInput == 'Your Orders':
                    print('You havent orederd anything yet.')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Discounts':
                    print('There are no discounts available at this time.')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Coupons':
                    print('You have no coupons right now.')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Pants':
            print('These are our Pants options. ')
            UserInput = input('Mens, Womens, Kids:  ')
            if UserInput == 'Mens':
                print(MensPants)
                UserInput = input('What pair of pants would you like to add to your cart:  ')
                if UserInput == 'BaggyJeans':
                    print('You have added a pair of baggy jeans to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Cargo':
                    print('You have added a pair of Cargo pants to your cart.   ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Kakis':
                    print('You have added a pair of kakis to your cart')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Womens':
                print(WomensPants)
                UserInput = input('What pair of pants would you like to add to your cart:  ')
                if UserInput == 'Leggings':
                    print('You have added a pair of leggings to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'SweatPants':
                    print('You have added a pair of sweatpants to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'HighwaistedJeans':
                    print('You have added a pair of Highwaisted jeans to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Kids':
                print(KidsPants)
                UserInput = input('What pair of pants would you like to add to your cart:  ')
                if UserInput == 'Sweat':
                    print('You have added a pair of sweatpants to your cart')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Cargo':
                    print('You have added a pair of cargo oants to tour cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Jeans':
                    print('You have added a pair of Jeans to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Shorts':
            print('These are our Shorts options.')
            UserInput = input('Mens, Womens, Kids:  ')
            if UserInput == 'Mens':
                print(MensShorts)
                UserInput = input('What pair of shorts would you like to add to your cart:  ')
                if UserInput == 'Baggy':
                    print('You have added a pair of Baggy shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Cargo':
                    print('Your have added a pair of CargoShorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Kaki':
                    print('You have added a pair of kakiShorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Womens':
                print(WomensShorts)
                UserInput = input('What pair of shorts would you like to add to your cart:  ')
                if UserInput == 'Compression':
                    print('You have added a pair of Compression shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Gym':
                    print('You have added a pair of Gym shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == "Jean":
                    print('You have added a pair of Jean Shorts to your cart. ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Kids':
                print(KidsShorts)
                UserInput = input('What pair of shorts would you like to add to your cart:  ')
                if UserInput == 'Gym':
                    print('You have added a pair of Gym shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Cargo':
                    print('You h ave added a pair of cargo shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Jean':
                    print('You have added a pair of Jean Shorts to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Shirts':
            print(Shirts)
            UserInput = input('What kind of shirts would you like to see:  ')
            if UserInput == 'Graphic':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white graphic shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black graphic shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey graphic shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Plain':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white plain shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black plain shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey plain shirt to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Sweaters':
            print(Sweaters)
            UserInput = input('What kind of sweaters would you like to see:  ')
            if UserInput == 'Graphic':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white graphic sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black graphic sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey graphic sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Plain':
                UserInput = input('Choose a color. White, Black, grey:  ')
                if UserInput == 'White':
                    print('You have added a white plain sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black plain sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey plain sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Hoodless':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white hoodless sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black hoodless sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey hoodless sweater to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
        elif UserInput == 'Coats':
            print(Coats)
            UserInput = input('What kind of coats would you like to see:  ')
            if UserInput == 'Puffer':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white puffer coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black puffer coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey puffer coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Hoodless':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white hoodless coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black hoodless coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey hoodless coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
            elif UserInput == 'Regular':
                UserInput = input('Choose a color. White, Black, Grey:  ')
                if UserInput == 'White':
                    print('You have added a white coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Black':
                    print('You have added a black coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)
                elif UserInput == 'Grey':
                    print('You have added a grey coat to your cart.  ')
                    UserInput = input('BackToHomePage:  ')
                if UserInput == 'yes':
                    print(HomePage)

HotMess()