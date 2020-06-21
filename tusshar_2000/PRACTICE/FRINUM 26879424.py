from collections import Counter
t=int(input())
while t>0:
    input()
    l=map(int,input().split())
    l=Counter(l)
    l=l.most_common()[:-2:-1][-1]
    if l[-1]==1:
        print(l[0])
    else:
        print("-1")
    t-=1