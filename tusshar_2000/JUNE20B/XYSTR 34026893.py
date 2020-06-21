t=int(input())
while t>0:
    s=input()
    if len(s)==1:
        print(0)
    else:
        i=0;j=1
        ans=0
        while j<len(s):
            if (s[i]=='x' and s[j]=='y') or (s[i]=='y' and s[j]=="x"):
                ans+=1
                i=j+1
                j=i+1
            else:
                i=j
                j=i+1
        print(ans)
    t-=1