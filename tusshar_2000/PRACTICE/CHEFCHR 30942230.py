t=int(input())
while t>0:
    i=input()
    count=0
    for index in range(len(i)):
        temp=i[index:index+4]
        if "".join(sorted(temp))=="cefh":
            count+=1
    if count!=0:
        print("lovely",count)
    else:
        print("normal")
    t-=1