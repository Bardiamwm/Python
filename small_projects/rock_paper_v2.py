from random import randint
import time
print("Welcom to Rock and paper Game \U0001F606\n")
input("press enter to start the Game...")
result = [0, 0]
while True:
    
    p1, p2 = (s := ["rock", "paper", "gheychy"])[randint(0, 2)], s[randint(0, 2)]
    
    for s in f"\nplayer 1: {p1}":
        print(s, end="", sep="")
        time.sleep(0.1)
    time.sleep(0.4)
    
    print("")
    
    for s in "------------------":
        print(s, end="", sep="")
        time.sleep(0.04)
    time.sleep(0.1)
    
    print("")    
    
    for s in f"player 2: {p2}":
        print(s, end="", sep="")
        time.sleep(0.1)
    time.sleep(0.4)

    print("")
    
    for s in "------------------":
        print(s, end="", sep="")
        time.sleep(0.04)
    time.sleep(0.4)
    
    print("")
    
    if p1 == "rock":
        if p2 == "rock":
            print("draw")
        
        elif p2 == "paper":
            print("player 2 Win")
            result[1] += 1
            
        else:
            print("player 1 Win")
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
            
    time.sleep(0.5)         
       
    print(f"{result[0]} - {result[1]}\n")
    time.sleep(0.5)
    
    if input("Agin: ").lower()[0] != "y":
        print("")
        break
    else:
        print("")

for s in "The end...":
    print(s, end="", sep="")
    if s == ".": 
        time.sleep(0.25)
    else:
        time.sleep(0.1)
time.sleep(0.75)