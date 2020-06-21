t=int(input())
while t>0:
    n,q=map(int,input().split())
    arr=[0]*(n+1)
    
    while q>0:
        l,r=map(int,input().split())
        arr[l-1]+=1
        arr[r]-=1
        q-=1
    for i in range(1,n+1):
        arr[i]+=arr[i-1]
    print(*arr[:n])
    t-=1