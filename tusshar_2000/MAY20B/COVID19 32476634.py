from sys import *
inp=stdin.readline
t=int(inp())
while t>0:
    n=int(inp())
    x=list(map(int,inp().split()))
    # dist=[(x[i+1]-x[i]) for i in rxnge(len(x)-1)]
    ans=[]
    for j in range(n):
        if j==0:
            count=1
            temp=j
            while temp<=n-2 and x[temp+1]-x[temp]<=2 :
                count+=1
                temp+=1
            ans.append(count)
        elif j==n-1:
            count=1
            temp=j
            while temp>=1 and x[temp]-x[temp-1]<=2:
                count+=1
                temp-=1
            ans.append(count)
        else:
            count=1
            temp=j
            while temp<=n-2 and x[temp+1]-x[temp]<=2:
                count+=1
                temp+=1
            temp=j
            while temp>=1 and x[temp]-x[temp-1]<=2:
                count+=1
                temp-=1
            ans.append(count)
    print(min(ans),max(ans))       
        
        
        
    
    t-=1



    