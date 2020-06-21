from sys import *
inp=stdin.readline
out=print
t=int(inp())
while t>0:
    n=int(inp())
    l=list(map(int,inp().split()))
    oddindex={ha:0 for ha,val in enumerate(l) if val%2!=0}
    eoddindex={va:0 for va,val in enumerate(l) if val%2==0 and val%4!=0}
    i=0;j=0;ans=0
    for mid in eoddindex:
        i=endi=mid
        while i-1 in oddindex:
            i-=1
        while endi+1 in oddindex:
            endi+=1
        ans+=(mid-i+1)*(endi-mid+1)
    out((n*(n+1)//2)-ans)
    t-=1