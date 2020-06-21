from sys import *
inp=stdin.readline
out=print
out1=stdout.flush
t=int(inp())
while t>0:
    n, p = map(int,inp().split())

    a = [[0 for _ in range(n)] for i in range(n)]
    a_copy = [[[[-1 for _ in range(n)] for i in range(n)] for __ in range(n)] for ___ in range(n)]
    out(1,1,1,n,n)
    out1()
    total=int(input())
    a_copy[0][0][n-1][n-1]=a_copy[0][n-1][0][n-1]=a_copy[n-1][0][n-1][0]=a_copy[n-1][n-1][0][0]=total
    i=0
    for _ in range(n//2):
        for j in range(n//2):
            if a_copy[i][j][n-1][n-1]==-1:
                out(1,i+1,j+1,n,n)
                out1()
                main_one=int(inp())
                a_copy[i][j][n-1][n-1]=main_one
                a_copy[i][n-1][n-1][j]=main_one
                a_copy[n-1][j][i][n-1]=main_one
                a_copy[n-1][n-1][i][j]=main_one

            else:
                main_one=a_copy[i][j][n-1][n-1]
            
            if a_copy[i+1][j+1][n-1][n-1]==-1:
                out(1,i+2,j+2,n,n)
                out1()
                main_short=int(inp())
                a_copy[i+1][j+1][n-1][n-1]=main_short
                a_copy[n-1][j+1][i+1][n-1]=main_short
                a_copy[i+1][n-1][n-1][j+1]=main_short
                a_copy[n-1][n-1][i+1][i+1]=main_short
            else:
                main_short=a_copy[i+1][j+1][n-1][n-1]
            
            if a_copy[i][j+1][n-1][n-1]==-1:
                out(1,i+1,j+2,n,n)
                out1()
                main_right=int(inp())
                a_copy[i][j+1][n-1][n-1]=main_right
                a_copy[i][n-1][n-1][j+1]=main_right
                a_copy[n-1][j+1][i][n-1]=main_right
                a_copy[n-1][n-1][i][j+1]=main_right
            else:
                main_right=a_copy[i][j+1][n-1][n-1]

            if a_copy[i+1][j][n-1][n-1]==-1:
                out(1,i+2,j+1,n,n)
                out1()
                main_down=int(inp())
                a_copy[i+1][j][n-1][n-1]=main_down
                a_copy[n-1][j][i+1][n-1]=main_down
                a_copy[i+1][n-1][n-1][j]=main_down
                a_copy[n-1][n-1][i+1][j]=main_down

            else:
                main_down=a_copy[i+1][j][n-1][n-1]
            
            a[i][j] = main_one + main_short - (main_right + main_down)
        
        i+=1
    
    i=0
    for _ in range(n//2):
        for j in reversed(range(n//2,n)):
            if a_copy[n-1][0][i][j]==-1:
                out(1,i+1,1,n,j+1)
                out1()
                main_one=int(inp())
                a_copy[n-1][0][i][j]=main_one
                a_copy[n-1][j][i][0]=main_one
                a_copy[i][0][n-1][j]=main_one
                a_copy[i][j][n-1][0]=main_one
            else:
                main_one=a_copy[n-1][0][i][j]
            
            if a_copy[n-1][0][i+1][j-1]==-1:
                out(1,i+2,1,n,j)
                out1()
                main_short=int(inp())
                a_copy[n-1][0][i+1][j-1]=main_short
                a_copy[n-1][j-1][i+1][0]=main_short
                a_copy[i+1][0][n-1][j-1]=main_short
                a_copy[i+1][j-1][n-1][0]=main_short
            else:
                main_short=a_copy[n-1][0][i+1][j-1]
            
            if a_copy[n-1][0][i][j-1]==-1:
                out(1,i+1,1,n,j)
                out1()
                main_right=int(inp())
                a_copy[n-1][0][i][j-1]=main_right
                a_copy[i][0][n-1][j-1]=main_right
                a_copy[n-1][j-1][i][0]=main_right
                a_copy[i][j-1][n-1][0]=main_right
            else:
                main_right=a_copy[n-1][0][i][j-1]

            if a_copy[n-1][0][i+1][j]==-1:
                out(1,i+2,1,n,j+1)
                out1()
                main_down=int(inp())
                a_copy[n-1][0][i+1][j]=main_down
                a_copy[i+1][0][n-1][j]=main_down
                a_copy[n-1][j][i+1][0]=main_down
                a_copy[i+1][j][n-1][0]=main_down
            else:
                main_down=a_copy[n-1][0][i+1][j]
            
            a[i][j] = main_one + main_short - (main_right + main_down)

        i+=1
    
    i=n-1
    for _ in range(n//2):
        for j in range(n//2):
            if a_copy[i][j][0][n-1]==-1:
                out(1,1,j+1,i+1,n)
                out1()
                main_one=int(inp())
                a_copy[i][j][0][n-1]=main_one
                a_copy[0][j][i][n-1]=main_one
                a_copy[i][n-1][0][j]=main_one
                a_copy[0][n-1][i][j]=main_one
            else:
                main_one=a_copy[i][j][0][n-1]
            
            if a_copy[i-1][j+1][0][n-1]==-1:
                out(1,1,j+2,i,n)
                out1()
                main_short=int(inp())
                a_copy[i-1][j+1][0][n-1]=main_short
                a_copy[0][j+1][i-1][n-1]=main_short
                a_copy[i-1][n-1][0][j+1]=main_short
                a_copy[0][n-1][i-1][j+1]=main_short
            else:
                main_short=a_copy[i-1][j+1][0][n-1]
            
            if a_copy[i][j+1][0][n-1]==-1:
                out(1,1,j+2,i+1,n)
                out1()
                main_right=int(inp())
                a_copy[i][j+1][0][n-1]=main_right
                a_copy[0][j+1][i][n-1]=main_right
                a_copy[i][n-1][0][j]=main_right
                a_copy[0][n-1][i][j+1]=main_right
            else:
                main_right=a_copy[i][j+1][0][n-1]

            if a_copy[i-1][j][0][n-1]==-1:
                out(1,1,j+1,i,n)
                out1()
                main_down=int(inp())
                a_copy[i-1][j][0][n-1]=main_down
                a_copy[0][j][i-1][n-1]=main_down
                a_copy[i-1][n-1][0][j]=main_down
                a_copy[0][n-1][i-1][j]=main_down
            else:
                main_down=a_copy[i-1][j][0][n-1]
            
            a[i][j] = main_one + main_short - (main_right + main_down)

        i-=1
    
    i=n-1
    for _ in range(n//2):
        for j in reversed(range(n//2,n)):
            if a_copy[0][0][i][j]==-1:
                out(1,1,1,i+1,j+1)
                out1()
                main_one=int(inp())
                a_copy[0][0][i][j]=main_one
                a_copy[i][0][0][j]=main_one
                a_copy[0][j][i][0]=main_one
                a_copy[i][j][0][0]=main_one
            else:
                main_one=a_copy[0][0][i][j]
            
            if a_copy[0][0][i-1][j-1]==-1:
                out(1,1,1,i,j)
                out1()
                main_short=int(inp())
                a_copy[0][0][i-1][j-1]=main_short
                a_copy[i-1][0][0][j-1]=main_short
                a_copy[0][j-1][i-1][0]=main_short
                a_copy[i-1][j-1][0][0]=main_short
            else:
                main_short=a_copy[0][0][i-1][j-1]
            
            if a_copy[0][0][i][j-1]==-1:
                out(1,1,1,i+1,j)
                out1()
                main_right=int(inp())
                a_copy[0][0][i][j-1]=main_right
                a_copy[0][j-1][i][0]=main_right
                a_copy[i][0][0][j-1]=main_right
                a_copy[i][j-1][0][0]=main_right
            else:
                main_right=a_copy[0][0][i][j-1]

            if a_copy[0][0][i-1][j]==-1:
                out(1,1,1,i,j+1)
                out1()
                main_down=int(inp())
                a_copy[0][0][i-1][j]=main_down
                a_copy[0][j][i-1][0]=main_down
                a_copy[i-1][0][0][j]=main_down
                a_copy[i-1][j][0][0]=main_down
            else:
                main_down=a_copy[0][0][i-1][j]
            
            a[i][j] = main_one + main_short - (main_right + main_down)
        
        i-=1
    
    print(2)
    out1()
    for i in a:
        out(*i)
        out1()
    if int(inp())==-1:
        break
    t-=1   