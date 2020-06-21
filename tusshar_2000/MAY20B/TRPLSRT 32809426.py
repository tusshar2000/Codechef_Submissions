from __future__ import print_function
from sys import *
inp=stdin.readline
out=stdout.write
str=str
input=input
len=len
int=int
map=map
t=int(inp())
while t>0:
    flag=0
    n,kk=map(int,inp().split())
    p=list(map(int,inp().split()))
    inplace={i:1 for i in range(n) if p[i]!=i+1}
    ans=[]
    previ=-1;prevj=-1;prevk=-1
    inplace1={}
    while inplace:
        try:
            i=next(iter(inplace))
            j=p[i]-1
            if p[j]==i+1:
                inplace1[i]=0
                inplace1[j]=0
                del inplace[i]
                del inplace[j]
                continue
            else:
                k=p[j]-1
        
            if previ==i and prevj==j and prevk==k: 
                flag=1
                break
            p[i],p[j],p[k]=p[k],p[i],p[j]
            ans.append([i+1,j+1,k+1])
            previ=i;prevj=j;prevk=k
            
            if p[i]==i+1:
                del inplace[i]
            if p[j]==j+1:
                del inplace[j]
            if p[k]==k+1:
                del inplace[k]
        except:
            flag=1
            break
    previ=-1; prevj=-1;prevk=-1
    while inplace1:
        try:
            i=next(iter(inplace1))
            j=p[i]-1
            if p[j]==i+1:
                k=i+1
                while p[k]==k+1 or k==j:
                    k+=1
                j,k=k,j
            else:
                k=p[j]-1
            if previ==i and prevj==j and prevk==k: 
                flag=1
                break
            p[i],p[j],p[k]=p[k],p[i],p[j]
            ans.append([i+1,j+1,k+1])
            previ=i;prevj=j;prevk=k
            
            if p[i]==i+1:
                del inplace1[i]
            if p[j]==j+1:
                del inplace1[j]
            if p[k]==k+1:
                del inplace1[k]
        except:
            flag=1
            break
    le=len(ans)
    if flag==1 or le>kk:
        out("-1"+"\n")
    elif le==0:
        out("0"+"\n")
    else:
        out(str(le)+"\n")
        for iii in ans:
            print(*iii)
           
    
    t-=1
    