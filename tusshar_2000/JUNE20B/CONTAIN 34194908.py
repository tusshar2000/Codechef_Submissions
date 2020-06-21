from __future__ import print_function
from functools import *
from sys import *
inp=stdin.readline
out=stdout.write
len=len
int=int
reduce=reduce
map=map
sorted=sorted
str=str
def main():
    # http://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
    #solution2(3D), solution3(3D)
    def ray_tracing_method(x,y,poly):
        
        n = len(poly)
        inside = True

        for i in range(n):
            p1x,p1y = poly[i]
            p2x,p2y = poly[(i+1) % n]
            d=(x-p1x)*(p2y-p1y) - (y-p1y)*(p2x-p1x)
            if d>=0:
                return False
        return inside

    # https://gist.github.com/arthur-e/5cf52962341310f438e96c1f3c3398b8
    def convex_hull(points):
        TURN_LEFT, TURN_RIGHT, TURN_NONE = 1, -1, 0
        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

        def _keep_left(hull, r):
            while len(hull) > 1 and (turn(hull[-2], hull[-1], r) == TURN_RIGHT):
                hull.pop()
            if not len(hull) or hull[-1] != r:
                hull.append(r)
            return hull

        l = reduce(_keep_left, points, [])
        u = reduce(_keep_left, points[::-1], [])
        return l.extend(u[i] for i in range(1, len(u) - 1)) or l

    t=int(inp())
    while t>0:
        n,q=map(int,inp().split())
        points=[0]*n
        n1=0
        while n1!=n:
            points[n1]=list(map(int,inp().split()))
            n1+=1
        
        points.sort()
        total_hull=[]
        while len(points)>=3:
            hull=convex_hull(points)
            total_hull.append(hull)
            points=[i for i in points if i not in hull]
        while q>0:
            p=list(map(int,inp().split()))
            count=0
            low=0
            high=len(total_hull)-1
            while low<=high:
                mid=(low+high)//2
                if ray_tracing_method(p[0],p[1],total_hull[mid]): 
                    low=mid+1
                else: 
                    high=mid-1
            out(str(low)+"\n")
            q-=1
        t-=1

if __name__=="__main__":
    main()
