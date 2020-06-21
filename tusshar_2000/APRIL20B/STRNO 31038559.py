from math import sqrt
from collections import *
from sys import *
from functools import *

def calcuans(x):
    res=[]
    while x%2==0: 
        res.append(2)
        x=x/2
        
    for i in range(3,int(sqrt(x))+1, 2): 
        while x%i==0: 
            res.append(i) 
            x=x/i 
    if x>2: 
        res.append(x) 
    return res
    
inp=stdin.readline
t=int(inp())
while t>0:
    x,k=map(int,inp().split())
    if len(calcuans(x))>=k:
        print("1")
    else:
        print("0")
    t-=1
    
