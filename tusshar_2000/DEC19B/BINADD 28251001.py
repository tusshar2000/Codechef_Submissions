from sys import stdin,stdout
s=stdin.readline
s1=stdout.write
def main():
    t=int(s())
    while t>0:
        A=int(s(),2)
        B=int(s(),2)
        count=0
   
        while B>0:
            U = A ^ B
            V = A & B
            A = U
            B = V * 2
            count+=1
    
        s1(str(count)+"\n")
        t-=1
if __name__== "__main__":
    main()