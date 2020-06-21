from sys import stdin, stdout
t=stdin.readline();t=int(t)
res=['0','1','2','3','4','5','6','7','8','9']
while t>0:
    l=list(stdin.readline())
    ans=sum(list(map(int,filter(lambda x:x in res,l))))
    stdout.write(str(ans)+'\n')
    t-=1