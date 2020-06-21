t=int(input())
while t>0:
    p_dict={}
    n=int(input())
    while n>0:
        p,s=map(int,input().split())
        if p==9 or p==10 or p==11:
            pass
        elif p not in p_dict:
            p_dict[p]=s
        elif p_dict[p]<s:
            p_dict[p]=s
            
        n-=1
    print(sum(p_dict.values()))
    t-=1