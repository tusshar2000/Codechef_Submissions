from sys import stdin,stdout
inp=stdin.readline
out=print
out1=stdout.flush
t=int(inp())
while t>0:
    n=int(inp())
    nval=10**n
    a=int(inp())
    s=2*nval + a
    out(s)
    out1()
    b=int(inp())
    c=nval - b
    out(c)
    out1()
    d=int(inp())
    e=nval - d
    out(e)
    out1()
    ans=int(inp())
    if ans==-1:
        break
    t-=1