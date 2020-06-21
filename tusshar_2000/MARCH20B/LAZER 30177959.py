#took help from geeksforgeeks
class repre: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
def Segon(p, q, r): 
    if ((q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False
  
def orient(p, q, r): 
    ans =(float(q.y - p.y)*(r.x - q.x))-(float(q.x - p.x)*(r.y - q.y)) 
    if ans>0: 
        return 1
    elif ans<0: 
        return -1
    else: 
        return 0

def doint(p1,q1,p2,q2): 
    o1 = orient(p1, q1, p2) 
    o2 = orient(p1, q1, q2) 
    o3 = orient(p2, q2, p1) 
    o4 = orient(p2, q2, q1) 
    if ((o1 != o2) and (o3 != o4)): 
        return True
    elif ((o1 == 0) and Segon(p1, p2, q1)): 
        return True
    elif ((o2 == 0) and Segon(p1, q2, q1)): 
        return True
    elif ((o3 == 0) and Segon(p2, p1, q2)): 
        return True
    elif ((o4 == 0) and Segon(p2, q1, q2)): 
        return True
    return False
 
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    div = det(xdiff, ydiff)
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

from sys import *
inp=stdin.readline
out=stdout.write
t=int(inp())
while t>0:
    n,q=map(int,inp().split())
    al=list(map(int,inp().split()))
    list_of_points=[[i+1,al[i]]for i in range(n)]
    while q>0:
        count=0
        x1,x2,y=map(int,inp().split())
        p2=repre(x1,y)
        q2=repre(x2,y)
        C=(x1,y)
        D=(x2,y)
        prev=(0,0)
        for i in range(n-1):
            p1=repre(list_of_points[i][0],list_of_points[i][1])
            q1=repre(list_of_points[i+1][0],list_of_points[i+1][1])
            A=(list_of_points[i][0],list_of_points[i][1])
            B=(list_of_points[i+1][0],list_of_points[i+1][1])
            
            if doint(p1,q1,p2,q2):
                ans=line_intersection((A,B),(C,D))
                if ans==prev:
                    pass
                else:
                    prev=ans
                    
                    count+=1
        out(str(count)+"\n")
        q-=1
    t-=1