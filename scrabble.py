import math
import enchant
import itertools

d = enchant.Dict("en_US")
v=""
w=""

def scrabble(v,m):
    for i in reversed(range(2,len(v)+1)):
        z=list(itertools.permutations(v,i))
        z=set(z)
        z=list(z)
        for j in range(0,len(z)):
            w=''.join(z[j])
            if(d.check(w)):
                if m in w:
                    return(w)


        
print "Input string was: blbearsc and word formed must contain e"
print " "
print "Word formed is: "+scrabble("blbearsc","e")
