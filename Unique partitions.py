class Solution:
    def dfs(self,n,s,l,m):
        if s==n:
            m.append(l)
            return
        if s>n:
            return
        for i in range(n,0,-1):
            if len(l)==0 or l[-1]>=i:
                self.dfs(n,s+i,l+[i],m)

    def UniquePartitions(self, n):
        m=[]
        self.dfs(n,0,[],m)
        return m
