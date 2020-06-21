from sys import stdin,stdout
inp=stdin.readline
out=stdout.write
t=int(inp())
while t>0:
    n=int(inp())
    print(int(360/(180-(2*n))))
    t-=1