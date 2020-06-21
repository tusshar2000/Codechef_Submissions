from collections import *
from sys import *
from functools import *
inp=stdin.readline
t=int(inp())
while t>0:
    n=int(inp())
    l=list(map(int,inp().split()))
    l.sort()
    ans=0
    # while l:
    #     ans+=l.pop()
    #     l=[i-1 for i in l if i>0]
    for i in range(n):
        l[i]=max(0,l[i]-n+(i+1))
        ans+=l[i]
    print(ans%(10**9 + 7))
    t-=1