from collections import *
from sys import *
inp=stdin.readline
out=print
t=int(inp())
while t>0:
    n=int(inp())
    A=list(map(int,inp().split()))
    B=list(map(int,inp().split()))
    A.sort()
    B.sort()
    ans=0
    for i in range(n):
        ans+=min(A.pop(),B.pop())
    print(ans)
    t-=1