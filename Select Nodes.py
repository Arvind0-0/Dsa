class Solution:
    def dfs(self, graph, u, p):
        exc, inc = 0, 1    
        for v in graph[u]:
            if v != p:
                cexc, cinc = self.dfs(graph, v, u)
                exc += cinc
                inc += min(cinc, cexc)
        return exc, inc
                
                
    def countVertex(self, N, edges):
        graph = [[] for _ in range(N)]
        for u,v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
            
        return min(self.dfs(graph, 0, -1))
