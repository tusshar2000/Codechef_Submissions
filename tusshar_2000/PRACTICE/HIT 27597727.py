inp=input
t=int(inp())
while t>0:
    flag=True
    n=int(inp())
    de=n//4
    l=list(map(int,inp().split()))
    l.sort()
    for i in range(de,n,de):
        if l[i-1]==l[i]:
            flag=False
            break
    if(flag):
        print(l[de],l[de*2],l[de*3])
    else:
        print("-1")
    t-=1