class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = r = cost = 0
        while l < len(colors):
            color_total = color_max = 0
            while r < len(colors) and colors[l] == colors[r]:
                color_total += neededTime[r]
                color_max = max(color_max, neededTime[r])
                r += 1
            cost += color_total - color_max
            l = r
        return cost