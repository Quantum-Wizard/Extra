import random
a=random.randint(1,100)
print("Welcome to The Guessing Game Challenge.\nThe game picks a random integer from 1 to 100, and the player guesses the number.\nThe Rules are:\n1. On a player's first turn, if their guess is within 10 of the number, 'Close!' will appear and if it is further than 10 away from the number, 'Far!' will appear.\n2. On all subsequent turns, if a guess is closer to the number than the previous guess, 'Closer!' will appear and if it is farther from the number than the previous guess, 'Further!' will appear.")
b=[]
c=int(input('Guess:'))
b.append(c)
d=a-c
if c in range(1,101):
    if abs(d)<=10 and c!=a:
        print("Close!")
    elif c==a:
        pass
    else:
        print("Far!")
else:
    print("Out of bound")
while c!=a:
    c=int(input('Guess:'))
    if c in range(1,101):
        b.append(c)
        if abs(b[-1]-a)<abs(b[-2]-a) and c!=a:
            print("Closer!")
        elif c==a:
            pass
        else:
            print("Further!")
    else:
        print("Out of bound")
else:
    print("Guessed correctly. Your total number of guesses are " + str(len(b)))
