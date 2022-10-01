import sys
from typing import List
class Solution:
    sys.setrecursionlimit(10**8)
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        seen = set()
        def dfs(x,y,sx,sy,curr):
            #print(x,y,curr)
            if x<0 or x>=n or y<0 or y>=m or grid[x][y]!=1:
                return 
            grid[x][y]=-1
            curr.append((x-sx,y-sy))
            dfs(x+1,y,sx,sy,curr)
            dfs(x-1,y,sx,sy,curr)
            dfs(x,y+1,sx,sy,curr)
            dfs(x,y-1,sx,sy,curr)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    curr = []
                    dfs(i,j,i,j,curr)
                    seen.add(tuple(curr))
        return len(seen)
