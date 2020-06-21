i=input
t=int(i())
while t>0:
    count=0
    n,p=map(int,i().split())
    l=list(map(int,i().split()))
    l.sort()
    s=sum(l)
    while s>p:
        s-=l[-1]
        del l[-1]
        count+=1
    print(n-count)
    t-=1