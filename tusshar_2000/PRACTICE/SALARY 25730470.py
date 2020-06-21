# cook your dish here
t=int(input())
while t>0:
    input()
    l=list(map(int,input().split()))
    print(sum(l)-len(l)*(min(l)))
    t-=1