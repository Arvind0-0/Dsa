class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        n = len(height)
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                j = stack.pop()
                if len(stack) == 0:
                    break
                h = min(height[i], height[stack[-1]]) - height[j]
                w = i - stack[-1] - 1
                ans += h * w

            stack.append(i)
        return ans