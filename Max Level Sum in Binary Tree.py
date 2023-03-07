class Solution:
    def maxLevelSum(self, root):
        max_sum = -1000000
        qu = []
        qu.append(root)
        while len(qu):
            l = len(qu)
            summ = 0
            while l:
                curr = qu.pop(0)
                summ+=curr.data
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
                l-=1
            max_sum = max(max_sum,summ)
        return max_sum
        
