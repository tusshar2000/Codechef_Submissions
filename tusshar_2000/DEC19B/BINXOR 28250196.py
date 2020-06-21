from itertools import permutations 
i=input
o=print
t=int(i())
while t>0:
    dic={}
    n=int(i())
    a=i()
    b=i()
    a=list(permutations(a,n)) 
    b=list(permutations(b,n)) 
    
    a2=list(set(list(int("".join(a1),2) for a1 in a)))
    b2=list(set(list(int("".join(b1),2) for b1 in b)))
    
    for w in a2:
        for w1 in b2:
            res=w^w1
            dic[res]=1
    
    o((len(dic))00000007)
    t-=1