from typing import List
from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque([])
        q.append((source, 0))
        grid[source[0]][source[1]] = 0
        while q:
            (r, c), count = q.popleft()
            if [r, c] == destination:
                return count
            for dr, dc in directions:
                row = r+dr
                col = c+dc
                if row not in range(rows) or col not in range(cols) or grid[row][col] == 0:
                    continue
                
                grid[row][col] = 0
                q.append(((row, col),count+1))
        return -1
