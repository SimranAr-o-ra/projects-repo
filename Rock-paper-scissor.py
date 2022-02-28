print("READY FOR ROCK,PAPER AND SCISSORS?")
import random 
randno= random.randint(1, 3)
if randno==1:
    comp= 'r'
elif randno==2:
    comp='p'
elif randno==3:
    comp='s'

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
              return True    
        

print("COMPUTER'S TURN: USE FOR ROCK- r,PAPER- p AND SCISSOR- s")
you=input("Yours TURN: USE FOR ROCK- r,PAPER- p AND SCISSOR- s\n")
print(f"Computer choose-{comp}")
a=gamewin(comp,you)
if a==None:
    print("Game is tie,play again!")
elif a:
    print("Congratulations, You Win")
else:
    print("You loose,play again")
