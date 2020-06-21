from collections import *
from sys import *
inp=stdin.readline
out=print
t=int(inp())
ans1=[]
while t>0:
    n=int(inp())
    A=[[0 for i in range(4)] for j in range(4)]
    while n>0:
        i,j=inp().split()
        j=int(j)
        if i=='A':
            if j==12:
                A[0][0]+=1
            elif j==3:
                A[0][1]+=1
            elif j==6:
                A[0][2]+=1
            else:
                A[0][3]+=1
        elif i=='B':
            if j==12:
                A[1][0]+=1
            elif j==3:
                A[1][1]+=1
                
            elif j==6:
                A[1][2]+=1
            else:
                A[1][3]+=1
        
        elif i=='C':
            if j==12:
                A[2][0]+=1
            elif j==3:
                A[2][1]+=1
            elif j==6:
                A[2][2]+=1
            else:
                A[2][3]+=1
        else:
            if j==12:
                A[3][0]+=1
            elif j==3:
                A[3][1]+=1
            elif j==6:
                A[3][2]+=1
            else:
                A[3][3]+=1
        
        n-=1
    listoflist=[]
    for aa in range(4):
        for bb in range(4):
            for cc in range(4):
                for dd in range(4):
                    listoflist.append(sorted([A[0][aa],A[1][bb],A[2][cc],A[3][dd]],reverse=True))
    finalanswer1=-1e8
    for i in listoflist:
        val=100
        finalanswer=0
        for j in i:
            finalanswer+=j*val
            val-=25
        anscounter=Counter(i)
        finalanswer-=100*anscounter[0]
        if finalanswer>finalanswer1:
            finalanswer1=finalanswer
    ans1.append(finalanswer1)
    print(finalanswer1)
    t-=1
print(sum(ans1))