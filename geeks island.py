from collections import deque
class Solution():
    def bfs(self, mat, n, m, src):
        Q = deque(src)
        visited = set(src)
        while Q:
            x, y = Q.popleft()
            for nx, ny in [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]:
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] >= mat[x][y] and (nx,ny) not in visited:
                    Q.append((nx, ny))
                    visited.add((nx,ny))
        return visited
            
        
    def water_flow(self, mat, n, m):
        visited1 = self.bfs(mat, n, m, [(i,0) for i in range(n)] + [(0,j) for j in range(m)])
        visited2 = self.bfs(mat, n, m, [(i,m-1) for i in range(n)] + [(n-1,j) for j in range(m)])
        return len(visited1 & visited2)
