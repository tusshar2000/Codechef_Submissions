# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

def minSwaps(arr): 
    n = len(arr) 
      

    arrpos = [*enumerate(arr)] 
      
 
    arrpos.sort(key = lambda it:it[1]) 
      

    vis = {k:False for k in range(n)} 

    ans = 0
    for i in range(n): 

        if vis[i] or arrpos[i][0] == i: 
            continue

        cycle_size = 0
        j = i 
        while not vis[j]: 

            vis[j] = True

            j = arrpos[j][0] 
            cycle_size += 1

        if cycle_size > 0: 
            ans += (cycle_size - 1) 
 
    return ans
    
from sys import stdin
inp=stdin.readline
input=input
for i in range(int(inp())):
    n,m=map(int,inp().split())
    print(minSwaps(list(map(int,inp().split()))))
