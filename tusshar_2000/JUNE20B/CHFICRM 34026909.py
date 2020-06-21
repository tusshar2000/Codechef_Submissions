from sys import *
inp=stdin.readline
t=int(inp())
while t>0:
    n=int(inp())
    a=list(map(int,input().split()))
    dic={5:0,10:0,15:0}
    flag=0
    for i in a:
        if i==5:
            dic[5]+=1
        elif i==10:
            dic[10]+=1
            if dic[5]>=1:
                dic[5]-=1
            else:
                flag=1
                break
        elif i==15:
            dic[15]+=1
            if dic[10]>=1:
                dic[10]-=1
            elif dic[5]>=2:
                dic[5]-=2
            else:
                flag=1
                break
    if flag!=1:
        print("YES")
    else:
        print("NO")
    t-=1