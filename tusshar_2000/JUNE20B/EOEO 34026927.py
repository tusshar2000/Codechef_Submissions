t=int(input())
while t>0:
    ts=int(input())
    if ts%2!=0:
        print(ts//2)
    else:
        while ts%2==0:
            ts//=2
        print(ts//2)
    t-=1