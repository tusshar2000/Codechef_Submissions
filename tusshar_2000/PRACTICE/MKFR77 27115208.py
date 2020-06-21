n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
for i in range(n):
    if l[i]>k:
        l=l[i:]
        break
print(len(l))