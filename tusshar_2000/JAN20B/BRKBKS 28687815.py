from sys import stdin

inp=stdin.readline
t=int(inp())
while t>0:
    lis=list(map(int,inp().split()))
    s=lis[0]
    w=lis[1:]
    su=0
    count=1
    for i in range(len(w)):
        su+=w[i]
        if su>s:
            su=w[i]
            count+=1
    print(count)
            
        
    t-=1