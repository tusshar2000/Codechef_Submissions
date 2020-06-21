t=int(input())
while t>0:
    n=int(input())
    j=0
    for i in range(n):
        if i%2==0:print(*[i+1 for i in range(i*(n-1)+i,i*(n-1)+i+n)])
        else:print(*[i+1 for i in reversed(range(i*(n-1)+i,i*(n-1)+i+n))])
    t-=1