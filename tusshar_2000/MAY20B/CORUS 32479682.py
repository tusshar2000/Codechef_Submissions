from collections import *
from sys import *
inp=stdin.readline
t=int(inp())
while t>0:
    n,q=map(int,inp().split())
    s=input()
    dic=defaultdict(int)
    for i in s:
        dic[i]+=1
    ans=len(dic)
    val=dic.values()
    while q>0:
        c=int(inp())
        finalans=[i-c for i in val if i>c]
        print(sum(finalans))
        q-=1
    
    t-=1



    