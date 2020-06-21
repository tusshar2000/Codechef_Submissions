import math
from sys import *
out=print
inp=stdin.readline
t=int(inp())
ans=[[8,8],[7,7],[6,8],[1,3],[3,1],[8,6],[7,5],[8,4],[4,8],[1,5],[5,1],[7,3],[8,2],[7,1],[1,7],[2,8]]
while t>0:
    r,c=map(int,inp().split())
    if r==1 and c==1:
        out(len(ans))
        for i in ans:
            out(*i)
    else:
        out(len(ans) + 2)
        if r<c:
            r,c=c,r
        answer=(r-c)//2
        out(r-answer,r-answer)
        out(1,1)
        for i in ans:
            out(*i)
    t-=1