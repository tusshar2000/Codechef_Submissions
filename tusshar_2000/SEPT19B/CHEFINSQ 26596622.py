from sys import stdin, stdout 
from itertools import combinations
from collections import Counter 
t=int(input().strip())
while(t>0):
    c=0
    N,K=map(int,stdin.readline().split())
    l=list(map(int,stdin.readline().split()))
    l.sort()
    l1=list(combinations(l,K))
    del(l)
    l1.sort(key = lambda x: x[0])
    cou=Counter(l1)
    stdout.write(str(cou[l1[0]]))
    stdout.write("\n")
    t-=1