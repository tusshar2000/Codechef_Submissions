from collections import *
from sys import *
inp=stdin.readline
t=int(inp())
while t>0:
    s=input()
    if len(s)%2==0:
        s1=Counter(s[:len(s)//2])
        s2=Counter(s[len(s)//2:])
    else:
        s1=Counter(s[:len(s)//2])
        s2=Counter(s[len(s)//2 + 1:])
    if Counter(s1)==Counter(s2):
        print("YES")
    else:
        print("NO")
    t-=1