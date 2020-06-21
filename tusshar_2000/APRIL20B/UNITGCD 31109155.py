from collections import *
from sys import *
from functools import *
inp=stdin.readline
t=int(inp())
while t>0:
    n=int(inp())
    if n<=3:
        print(1)
        l=[i for i in range(1,n+1)]
        print(len(l),*l)
    else:
        l=[[1,2,3]]
        if (n-3)%2==0:
            for i in range(4,n+1,2):
                l.append([i,i+1])
        else:
            l.append([n])
            for i in range(4,n,2):
                l.append([i,i+1])
        print(len(l))
        for i in l:
            print(len(i),*i)

    t-=1