from collections import Counter
from sys import stdin
inp=stdin.readline
t=int(inp())
while t>0:
    n=int(inp())
    l=list(map(int,inp().split()))
    l_co=Counter(l)
    l_co=l_co.most_common(1)
    print(n-l_co[0][1])
    
    
    
    t-=1