# cook your dish here
t=int(input())
while(t>0):
    N,K=map(int,input().split())
    lang=input().split();test=[]
    for _ in range(K):
        ti=input().split()
        test+=ti[1:]
    a=""
    for i in lang:
        if i in test:
            a+='YES '
        else:
            a+='NO '
    print(a)
    t-=1