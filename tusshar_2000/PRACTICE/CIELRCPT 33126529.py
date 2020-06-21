import math
from sys import *
inp=stdin.readline
f=0
if not f:
    out=print
else:
    out=stdout.write
    
def linp(x):
    return list(map(int,x.split()))
def minp(x):
    return map(int,x.split())

t=int(inp())
while t>0:
    p=int(inp())
    res=0
    while True:
        i=0
        while i<12 and 2**i<=p:
            i+=1
        p-=2**(i-1)
        res+=1
        if 0==p:
            out(res)
            break
    
    t-=1