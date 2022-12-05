	def nearest(self, grid):
		
		def bfs(r, c):
		    q = [(r, c)]
		    steps = 0
		    while q:
		        nq = []
		        for r0, c0 in q:
		            if grid[r0][c0] == 1:
		                return steps 
		            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
		                r = r0+dr
		                c = c0+dc
		                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
		                    continue
		                nq.append((r, c))
		        steps += 1
		        q = nq
		    return -1
		
		ans = [[0]*len(grid[0]) for _ in range(len(grid))]
		for r in range(len(grid)):
		    for c in range(len(grid[0])):
		        ans[r][c] = bfs(r, c)
		return ans
