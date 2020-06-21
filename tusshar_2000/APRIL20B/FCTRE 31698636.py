import math
from collections import *
from sys import *
inp=stdin.readline
out=print

def calcuans(x):
    res=[]
    while x%2==0: 
        res.append(2)
        x/=2
    for i in range(3,int(math.sqrt(x))+1, 2): 
        while x%i==0: 
            res.append(i) 
            x/=i 
    if x>2: 
        res.append(int(x)) 
    return res

def dfs(visited, graph, node, d):
    if node not in visited:
        visited[node]=0
        for neighbour in graph[node]:
            if parent[neighbour]==0:
                parent[neighbour]=node
                depth[neighbour]=d+1
            dfs(visited, graph, neighbour, d+1)

def lca(a,b):
    path1=[a]
    path2=[b]
    while a!=b:
        if depth[a]<depth[b]:
            b=parent[b]
            path2.append(b)
        elif depth[a]>depth[b]:
            a=parent[a]
            path1.append(a)
        else:
            a=parent[a]
            b=parent[b]
            path1.append(a)
            path2.append(b)
    return path1[:len(path1)-1]+path2
    
t=int(inp())
while t>0:
    n=int(inp())
    
    visited={}
    parent=[0]*(n+1)
    depth=[0]*(n+1)
    graph=defaultdict(set)
    
    while n-1:
        x,y=map(int,inp().split())
        graph[x].add(y)
        graph[y].add(x)
        n-=1
        
    dfs(visited,graph,1,0)
    parent[1]=0
    depth[1]=0
    weight=list(map(int,inp().split()))
    weightfactor=[]

    for i in weight:
        weightfactor.append(calcuans(i))
    del weight
    query=int(inp())
    while query:
        a,b=map(int,inp().split())
        res=[]
        ans=lca(a,b)
        for i in ans:
            res+=weightfactor[i-1]
            
        cou=Counter(res)
        finalans=1
        for val in cou:
            finalans=(finalans*(cou[val]+1))%(10**9+7)
        out(finalans)
        query-=1
    t-=1


