import random
from collections import *
from sys import *
inp=stdin.readline
out=print
max1=float("inf")

t=int(inp())
while t>0:
    n,m,k=map(int,inp().split())
    list1=[list(map(int,inp().split())) for row in range(n)]
    finalanswerlist=[0 for _ in range(n)]
    pointer=0
    ans=m
    nigavg=[0 for _ in range(k)]
    for row in range(n):
        min1=max1
        co=Counter(list1[row])
        finalanswerlist[row]=list1[row][pointer]
        for column in range(k):
            if list1[row][column]==finalanswerlist[row]: 
                nigavg[column]+=n
            if nigavg[column]<min1:
                min1=nigavg[column];pointer=column
        ans^=random.randint(1,m)
    ans*=finalanswerlist[0]
    out(*finalanswerlist)
    t-=1




