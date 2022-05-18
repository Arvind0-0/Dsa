class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)
        arrives, crits = [None]*n, []
        def dfs(node = 0, parent = -1, time = 1):
            if arrives[node]: return
            arrives[node] = time
            for neighbor in graph[node]:
                if neighbor == parent: continue
                dfs(neighbor, node, time + 1)
                if arrives[neighbor] == time + 1: crits.append((node, neighbor))
                else: arrives[node] = min(arrives[node], arrives[neighbor])
            return crits
        return dfs()
