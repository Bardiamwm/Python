from random import randint
import time
print("Welcom to Rock and paper Game\n")
input("press enter to start the Game...")
result = [0, 0]
while True:
    
    p1, p2 = (s := ["rock", "paper", "gheychy"])[randint(0, 2)], s[randint(0, 2)]
    
    print(f"player 1: {p1}\n------------------")
    time.sleep(0.49)
    
    print(f"player 2: {p2}\n------------------")
    time.sleep(0.4)
    
    if p1 == "rock":
        if p2 == "rock":
            print("draw")
        
        elif p2 == "paper":
            print("player 2 Win")
            result[1] += 1
            
        else:
            print("plaayer 1 Win")
            result[0] += 1
            
    elif p1 == "paper":
        if p2 == "rock":
            print("player 1 Win")
            result[0] += 1
            
        elif p2 == "paper":
            print("draw")
        
        else: 
            print("player 2 Win")
            result[1] += 1
    else:
        if p2 == "rock":
            print("player 2 Win")
            result[1] += 1
            
        elif p2 == "paper":
            print("player 1 Win")
            result[0] += 1
            
        else:
            print("draw")
            
    print(f"{result[0]} - {result[1]}")
    
    if input("Agin: ").lower()[0] != "y":
        break

print("The end")
time.sleep(1)