import collections
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node: int, parent: int):
            counter = collections.Counter()
            for child in tree[node]:
                if child == parent: continue
                counter += dfs(child, node)
            counter[labels[node]] += 1
            result[node] = counter[labels[node]]
            return counter

        tree = collections.defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        result = [0] * n
        dfs(0, None)
        return result
