    def uniquePaths(self, n, m, grid):
        # code here 
        for i in range(1,n):
            if grid[i][0]==1:
               grid[i][0]=grid[i-1][0]
        for i in range(1,m):
            if grid[0][i]==1:
               grid[0][i]=grid[0][i-1]    
        for i in range(1,n):
            for j in range(1,m):
                if grid[i][j]==1:
                    a=b=0
                    if i-1>-1:
                        a=grid[i-1][j]
                    if j-1>-1:
                        b=grid[i][j-1]
                    # if a+b>0   : 
                    grid[i][j]=a+b    
                    grid[i][j]%=(10**9+7)
        # print(grid)            
        return grid[n-1][m-1] 
