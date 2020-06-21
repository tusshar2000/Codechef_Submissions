for _ in range(int(input())):
    X,Y,K,N=map(int,input().split())
    P=[];C=[]
    for _ in range(N):
        p,c=map(int,input().split())
        P.append(p);C.append(c)
    for j in range(len(P)):
        if K>=C[j] and X-Y<=P[j]:
            print("LuckyChef")
            break
    else:
        print("UnluckyChef")