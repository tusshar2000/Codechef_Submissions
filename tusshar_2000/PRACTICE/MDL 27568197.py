t=int(input())
while t>0:
    input()
    l=list(map(int,input().split()))
    max_list_index=l.index(max(l))
    min_list_index=l.index(min(l))
    if max_list_index<min_list_index:
        print(max(l),min(l))
    else:
        print(min(l),max(l))
    t-=1