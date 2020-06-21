t=int(input())
while t>0:
    s=input()
    if '1000' in s[-4:]:
        print("YES")
    else:
        print("NO")
    t-=1