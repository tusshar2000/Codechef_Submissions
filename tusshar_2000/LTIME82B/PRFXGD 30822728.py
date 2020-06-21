t=int(input())
while t>0:
    s=input()
    k,x=map(int,input().split())
    dic={}
    flag=0
    count=0
    for i in s:
        if i not in dic:
            count+=1
            dic[i]=1
        else:
            if dic[i]<x:
                dic[i]+=1
                count+=1
            elif dic[i]>=x and k!=0:
                k-=1
            elif dic[i]>=x and k==0:
                print(count)
                flag=1
                break
    if flag==0:
        print(count)
            
    t-=1