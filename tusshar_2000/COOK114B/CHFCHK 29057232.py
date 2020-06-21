from collections import *
from sys import *
inp=stdin.readline
out=print
t=int(inp())
while t>0:
    n=int(inp())
    nl=list(map(int,inp().split()))
    print(min(nl))
    t-=1