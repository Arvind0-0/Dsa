 def goodStones(self, n, arr) -> int:
        
        visited = [0]*n
        def dfs(i):
 
            nonlocal arr, visited, n
            if i < 0 or i >= n:
                return True
                
            if visited[i] > 0:
                return visited[i] == 2

            visited[i] = 1
            if dfs(i+arr[i]):
                visited[i] = 2
                return True
            return False
            
        
        return sum(dfs(i) for i in range(n))
