from collections import *
from sys import *
inp=stdin.readline
out=print
t=int(inp())
while t>0:
    n,target=map(int,inp().split())
    nl=list(map(int,inp().split()))
    ar1=[0]*n
    ans=""
    flag=0
    copytarget=target
    nl.reverse()
    for i in range(n):
        if copytarget<0:
            ar1.reverse()
            ans=" ".join(map(str,ar1))
            print("YES",ans)
            flag=1
            break
        elif copytarget%nl[i]==0:
            ar1[i]=copytarget//nl[i] - 1
            copytarget=copytarget-((copytarget//nl[i] - 1)*nl[i])  
       
        elif copytarget%nl[i]!=0:
            ar1[i]=copytarget//nl[i] + 1
            copytarget=copytarget-((copytarget//nl[i] + 1)*nl[i])
            
    if copytarget<0 and flag==0:
        ar1.reverse()
        ans=" ".join(map(str,ar1))
        print("YES",ans)
            
    elif copytarget>=0:
        print("NO")
            
    t-=1