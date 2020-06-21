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

n,d=minp(inp())
l=[0]*n
for i in range(n):
    l[i]=int(inp())
l.sort()
i=0
ans=0
while i<n-1:
    if l[i+1]-l[i]<=d:
        ans+=1
        i+=2
    else:
        i+=1
out(ans)