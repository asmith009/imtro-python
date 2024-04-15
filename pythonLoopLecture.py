# Answer 1. The difference between a for loop and a while loop is that a for loop continues with a limit, and a while loop continues forever if the condition is true.
# Answer 2. An example for a for loop would be like a book bag, or an inventory in a game. And an example for a while loop would be like traffic lights.


# Answer 3.

def LoopNumber_Counter():
    Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for evenNumber in Numbers:
        if Numbers == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]:
            print('This number is even')
            continue
        print(evenNumber)
LoopNumber_Counter()
