t=int(input())
while t>0:
    count0=count2=0
    input()
    l=list(map(int,input().split()))
    for i in l:
        if i==0:
            count0+=1
        elif i==2:
            count2+=1
    print(((count0)*(count0-1))//2 + (count2)*(count2-1)//2)
    t-=1