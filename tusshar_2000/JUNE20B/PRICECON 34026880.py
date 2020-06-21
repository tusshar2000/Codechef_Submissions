t=int(input())
while t>0:
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    ans1=sum(i for i in l if i<=k);ans2=sum(k for i in l if i>k)
    print(sum(l)-ans1-ans2)
    t-=1
