from collections import *
from sys import *
t=int(input())
while t>0:
    n=int(input())
    s=input()
    s+="z"
    l=[0,0]
    for i in range(n):
        if (s[i-1]=="L" and s[i]=="L") or (s[i-1]=="R" and s[i]=="R") or (s[i-1]=="U" and s[i]=="U") or (s[i-1]=="D" and s[i]=="D") or (s[i-1]=="L" and s[i]=="R") or (s[i-1]=="U" and s[i]=="D") or (s[i-1]=="R" and s[i]=="L") or (s[i-1]=="D" and s[i]=="U"):
            pass
        elif s[i]=="L":
            l[0]=l[0]-1
        elif s[i]=="R":
            l[0]+=1
        elif s[i]=="U":
            l[1]+=1
        else:
            l[1]-=1
    print(*l)
            
            
    
    t-=1