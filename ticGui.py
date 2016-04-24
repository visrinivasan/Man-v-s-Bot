import tic
import random

a="BBBBBBBBB"

print "Welcome to play Tic-Tac-Toe made by Team Intelli5"
e=random.randint(0,1)
if e==0:
    print "Robot plays first and chooses X to play"
    z="X"
    y="O"
else:
    y=input("You play first please enter X or O ")
    if y=="X":
        z="O"
    else:
        z="X"

while (1):
    while e==0:
        a=tic.tictactoe(a,z)
        if "Y" in a:
            print "You win. Game end is "
            print a[0:3]
            print a[3:6]
            print a[6:9]
            break
        if "R" in a:
            print "You loose. Game end is "
            print a[0:3]
            print a[3:6]
            print a[6:9]
            break
        else:
            print "Robot played. Game is "
            print a[0:3]
            print a[3:6]
            print a[6:9]
            num=input("Your turn, enter position number you want to play")
            a=list(a)
            a[num]=y
            a="".join(a)
            print "You played. Game is "
            print a[0:3]
            print a[3:6]
            print a[6:9]
    while e==1:
        num=input("Your turn, enter position number you want to play")
        a=list(a)
        a[num]=y
        a="".join(a)
        print "You played. Game is "
        print a[0:3]
        print a[3:6]
        print a[6:9]
        a=tic.tictactoe(a,z)
        if "Y" in a:
            print "You win. Game end is "
            print a[0:3]
            print a[3:6]
            print a[6:9]
            break
        if "R" in a:
            print "You loose. Game end is "
            print a[0:3]
            print a[3:6]
            print a[6:9]
            break
        print "Robot played. Game is "
        print a[0:3]
        print a[3:6]
        print a[6:9]        
    print "Bye. Play well Stay well!!!"
    break
        
        
    
    
    
