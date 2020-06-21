from collections import *
from sys import *
inp=stdin.readline
out=print

def sol(ans,alist,blist):
    for i in ans:
        if i[0]>=i[1]:
            return "NO"
            
    for i in range(1,n):
        if alist[i] in alist[:i] or alist[i] in blist[:i]:
            pass
        else:
            return "NO"
    if flag==0:
        return "YES"

t,s=map(int,inp().split())
while t>0:
    n=int(inp())
    alist=list(map(int,inp().split()));alist.sort()
    blist=list(map(int,inp().split()));blist.sort()
    ans=zip(alist,blist)
    flag=0
    if s==1:
        out(sol(ans,alist,blist))
    else:
        #if attacker gives up all cards are discarded
        #if defender gives up he takes up all the cards
        aset=set(alist)
        bset=set(blist)
        if len(aset)==1 and alist>blist:
            out("NO")
        elif alist==blist:
            out("NO")
        else:
            out("YES")
            
    t-=1