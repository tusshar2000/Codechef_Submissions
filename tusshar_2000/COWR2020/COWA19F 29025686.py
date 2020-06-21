from collections import *
from sys import *
inp=stdin.readline
out=print
t=int(inp())
while t>0:
    n=list(inp())
    n.sort(reverse=True)
    ans="".join(n)
    print(ans)
    t-=1
