class Solution():
    def maxWeightCell(self, N, Edge):
        weight = [0]*N
        for i in range(N):
            if Edge[i] != -1:
                weight[Edge[i]] += i
        mx = max(weight)
        return [i for i,n in enumerate(weight) if n==mx][-1]
