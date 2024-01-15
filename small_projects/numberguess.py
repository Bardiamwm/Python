import random
guess = random.randint(1, 1)
while True:
    n = int(input("enter your guess: "))
    if n == guess:
        print("True")
    else:
        print("False")
    if input("countinue? ").lower()[0] != "y": break