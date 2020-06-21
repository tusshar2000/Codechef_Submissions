import math
from collections import *
from sys import *
inp=stdin.readline
t=int(inp())
while t>0:
    n,m=map(int,inp().split())
    f=list(map(int,inp().split()))
    p=list(map(int,inp().split()))
    dic={}
    for i in range(n):
        if f[i] in dic:
            dic[f[i]]+=p[i]
        else:
            dic[f[i]]=p[i]
    print(min(dic.values()))
    
        
        
    t-=1