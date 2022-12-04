
class Solution:
    def shotestPath(self, grid, n, m, k):
        start = (0, 0, k)
        q = [start]
        visited = {(0, 0): k}
        
        steps = 0
        while q:
            nq = []
            for r0, c0, k0 in q:
                if r0 == n-1 and c0 == m-1:
                    return steps
                    
                nk = k0-grid[r0][c0]
                if nk < 0:
                    continue
                
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    r = r0+dr
                    c = c0+dc
                    if r < 0 or r >= n or c < 0 or c >= m:
                        continue
                    if (r,c) not in visited or visited[r, c] < nk:
                        visited[r, c] = nk
                        nq.append((r, c, nk))
            steps += 1
            q = nq
        return -1
