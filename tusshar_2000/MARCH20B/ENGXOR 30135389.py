from collections import *
from sys import *
inp=stdin.readline
out=stdout.write
st=str
numss_tooo_bitsss =[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
def couc(i): 
    nibba = 0
    if(0 == i): return numss_tooo_bitsss[0]
    nibba = i & 0xf 
    return numss_tooo_bitsss[nibba] + couc(i >> 4)
t=int(inp())
while t>0:
    n,q=map(int,inp().split())
    a_list=list(map(int,inp().split()))
    even=0;odd=0
    for i in a_list:
        if couc(i)%2==0:
            even+=1
        else:
            odd+=1
    even=st(even);odd=st(odd)
    while q>0:
        if couc(int(inp()))%2==0:
            out(" ".join([even,odd])+"\n")
        else:
            out(" ".join([odd,even])+ "\n")
        
        q-=1
    t-=1