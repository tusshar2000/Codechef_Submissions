from sys import stdin, stdout 
t=stdin.readline();t=int(t)
n=str
while t>0:
    l,r=map(int,stdin.readline().split());c=0
    for i in range(l,r+1):
        i=str(i)
        if i[-1]=='2' or i[-1]=='3' or i[-1]=='9':
            c+=1
    t-=1
    del(l);del(r)
    c=n(c)
    stdout.write(c)
    stdout.write("\n")
    del(c)