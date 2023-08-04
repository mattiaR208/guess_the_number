import random
import time

print("Guess the number: the game!")
print("Try to guess a number")

def still():
    w = input("Do you still want to play?(yes)(no): ")
    if w == "yes":
        guess()
    elif w == "no":
        exit()
    else:
        print("I guess you're playing too much...")
        time.wait(2)
        exit()
def guess():
    def easy_mode():
            c = random.randint(1, 6)
            b = int(input("Choose a number between 1 and 6: "))
            if c == b:
                e = input("You won! Want to play again?(yes)(no): ")
                if e  == "yes":
                    guess()
                elif e  == "no":
                    exit()
                else:
                    print("Incorrect.")
                    still()
            else:
                print("Wrong.")
                easy_mode()
    a = str(input('Choose game mode(easy)(medium)(hard): '))
    if a == "easy":
        easy_mode()    
        def medium_mode():
            c = random.randint(1, 20)
            b = int(input("Choose a number between 1 and 20: "))
            if c == b:
                e = input("You won! Want to play again?(yes)(no): ")
                if e  == "yes":
                    guess()
                elif e  == "no":
                    exit()
                else:
                    print("Incorrect.")
                    still()
            else:
                input("Wrong. Retry: ")
                medium_mode()                   
    elif  a  == "medium":
        medium_mode()
        def hard_mode():
            c = random.randint(1, 50)
            b = int(input("Choose a number between 1 and 50: "))
            if c == b:
                e = input("You won! Want to play again?(yes)(no): ")
                if e  == "yes":
                    guess()
                elif e  == "no":
                    exit()
                else:
                    print("Incorrect.")
                    still()
            else:
                input("Wrong. Retry: ")
                hard_mode()
    elif a == "hard":
        hard_mode()    
    else:
        print("Invalid.")
        guess() 

guess()