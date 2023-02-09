class Solution:

    def maximumMatch(self,G):

        m, n = len(G), len(G[0])

        match = [-1] * n

        visited = [False] * n

        def dfs(i):

            for j in range(n):

                if G[i][j] and not visited[j]:

                    visited[j] = True

                    if match[j] == -1 or dfs(match[j]):

                        match[j] = i

                        return True

            return False

        count = 0

        for i in range(m):

            visited = [False] * n

            if dfs(i):

                count += 1

        return count
