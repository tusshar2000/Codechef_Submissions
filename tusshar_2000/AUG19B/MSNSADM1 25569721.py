for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=[]
    for i in range(n):
        C.append((A[i]*20)-(B[i]*10))
        if C[i]<0:
            C[i]=0
    print(max(C))