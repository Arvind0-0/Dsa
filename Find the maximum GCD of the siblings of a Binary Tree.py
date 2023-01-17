import math

class Solution:

    def helper(self, node):
        q = [node]

        while q:
            nq = []
            for i in q:
                if i.left and i.right:
                    val = math.gcd(i.left.data, i.right.data)
                    if self.gcd <= val: self.gcd, self.res = val, i.data
                if i.left: nq.append(i.left)
                if i.right: nq.append(i.right)
            q=nq

    def maxGCD(self, root):
        if root is None: return -1
        self.gcd, self.res = float("-inf"), 0
        self.helper(root)
        return self.res
