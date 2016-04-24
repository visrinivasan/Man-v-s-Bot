import random
import re

def tictactoe(a, z):
    if(z=='X'):
        y='O'
    else:
        y='X'

    w=findAllZ(a,z)
    x=findAllY(a,y)
    c=playerWin(x)
    if c==1:
        a=list(a)
        a.extend(["Y"])
        a="".join(a)
        return a


    t=priority(a,w)
    if t==-1:
        q=priority(a,x)
        if q==-1:
            while(1):
                r=random.randint(0,8)
                if a[r]=="B":
                    a=list(a)
                    a[r]=z
                    a="".join(a)
                    return a
        else:
            a=list(a)
            a[q]=z
            a="".join(a)
            return a
    else:
        a=list(a)
        a[t]=z
        a.extend(["R"])
        a="".join(a)
        return a

def findAllZ(a,z):
    return [m.start() for m in re.finditer(z, a)]

def findAllY(a,y):
    return [m.start() for m in re.finditer(y, a)]

def priority(a,v):
    if 0 in v and 4 in v and a[8]=="B":
        return 8
    elif 4 in v and 8 in v and a[0]=="B":
        return 0
    elif 0 in v and 8 in v and a[4]=="B":
        return 4

    elif 2 in v and 4 in v and a[6]=="B":
        return 6
    elif 4 in v and 6 in v and a[2]=="B":
        return 2
    elif 2 in v and 6 in v and a[4]=="B":
        return 4
    
    elif 0 in v and 1 in v and a[2]=="B":
        return 2
    elif 1 in v and 2 in v and a[0]=="B":
        return 0
    elif 0 in v and 2 in v and a[1]=="B":
        return 1

    elif 3 in v and 4 in v and a[5]=="B":
        return 5
    elif 4 in v and 5 in v and a[3]=="B":
        return 3
    elif 3 in v and 5 in v and a[4]=="B":
        return 4

    elif 6 in v and 7 in v and a[8]=="B":
        return 8
    elif 7 in v and 8 in v and a[6]=="B":
        return 6
    elif 6 in v and 8 in v and a[7]=="B":
        return 7

    elif 0 in v and 3 in v and a[6]=="B":
        return 6
    elif 3 in v and 6 in v and a[0]=="B":
        return 0
    elif 0 in v and 6 in v and a[3]=="B":
        return 3

    elif 1 in v and 4 in v and a[7]=="B":
        return 7
    elif 4 in v and 7 in v and a[1]=="B":
        return 1
    elif 1 in v and 7 in v and a[4]=="B":
        return 4

    elif 2 in v and 5 in v and a[8]=="B":
        return 8
    elif 5 in v and 8 in v and a[2]=="B":
        return 2
    elif 2 in v and 8 in v and a[5]=="B":
        return 5

    else:
        return -1
    

def playerWin(v):
    if 0 in v and 4 in v and 8 in v:
        return 1
    elif 4 in v and 8 in v and 0 in v:
        return 1
    elif 0 in v and 8 in v and 4 in v:
        return 1

    elif 2 in v and 4 in v and 6 in v:
        return 1
    elif 4 in v and 6 in v and 2 in v:
        return 1
    elif 2 in v and 6 in v and 4 in v:
        return 1
    
    elif 0 in v and 1 in v and 2 in v:
        return 1
    elif 1 in v and 2 in v and 0 in v:
        return 1
    elif 0 in v and 2 in v and 1 in v:
        return 1

    elif 3 in v and 4 in v and 5 in v:
        return 1
    elif 4 in v and 5 in v and 3 in v:
        return 1
    elif 3 in v and 5 in v and 4 in v:
        return 1

    elif 6 in v and 7 in v and 8 in v:
        return 1
    elif 7 in v and 8 in v and 6 in v:
        return 1
    elif 6 in v and 8 in v and 7 in v:
        return 1

    elif 0 in v and 3 in v and 6 in v:
        return 1
    elif 3 in v and 6 in v and 0 in v:
        return 1
    elif 0 in v and 6 in v and 3 in v:
        return 1

    elif 1 in v and 4 in v and 7 in v:
        return 1
    elif 4 in v and 7 in v and 1 in v:
        return 1
    elif 1 in v and 7 in v and 4 in v:
        return 1

    elif 2 in v and 5 in v and 8 in v:
        return 1
    elif 5 in v and 8 in v and 2 in v:
        return 1
    elif 2 in v and 8 in v and 5 in v:
        return 1

    else:
        return 0

#print tictactoe("OBBBBBBXO","O")
