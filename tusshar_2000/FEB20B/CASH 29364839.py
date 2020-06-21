from collections import *
from sys import *
inp=stdin.readline
out=print
t=int(inp())
while t>0:
    n,k=map(int,inp().split())
    A=list(map(int,inp().split()))
    B=[i%k for i in A]
    print(sum(B)%k)
    t-=1