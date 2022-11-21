class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows,cols = len(maze),len(maze[0])
        start = tuple(entrance)
        q  = deque([start])
        res = 0
        visit = set([start])
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if [r,c]!= entrance and (r==0  or c==0 or r==rows-1 or c==cols-1):
                    return res
                for dr,dc in [(1,0),(-1,0),(0,-1),(0,1)]:
                    row,col = r+dr,c+dc
                    if 0<=row<rows and 0<=col<cols and maze[row][col] == "." and (row,col) not in visit:
                        q.append((row,col))
                        visit.add((row,col))
            res+=1
        return -1
        
