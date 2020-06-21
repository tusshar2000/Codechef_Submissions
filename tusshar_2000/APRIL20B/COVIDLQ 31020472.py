from collections import *
from sys import *
from functools import *
inp=stdin.readline
t=int(inp())
while t>0:
    n=int(inp())
    l=list(map(int,inp().split()))
    indices = [i for i, x in enumerate(l) if x == 1]
    for i in range(1,len(indices)):
        if indices[i]-indices[i-1]<6:
            print("NO")
            break
    else:
        print("YES")
    t-=1