import math
from sys import *
inp=stdin.readline
out=stdout.write
t=int(inp())
while t>0:
    x,y,l,r=map(int,inp().split())
    #subtask 1
    if x>y:
        x,y=y,x
    if x==0 or y==0 or r==0:
        print(l)
    elif l==0 and r>=2*y:
        print(x|y)
    else:
        temp=(x&r)*(y&r)
        max1=r
        msb=r.bit_length()
        r=bin(r)[2:]
        le=len(r)
        # print(msb,le,r[-msb])
        while r[-msb]=="1":
            i=-1
            while r[i]!="1":
                i-=1
            r=r[:i]+"0"+"1"*(le-len(r[:i])-1)
            # print(r)
            intr=int(r,2)
            temp1=(x&intr)*(y&intr)
            if temp1>=temp:
                temp=temp1
                max1=intr
        print(max1)
    
        

        
        
        
    t-=1




    



    