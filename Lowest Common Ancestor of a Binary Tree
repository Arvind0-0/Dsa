class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def helper(node):
            nonlocal res
            if not node:
                return False
            l = helper(node.left)
            r = helper(node.right)
            mid = node == p or node == q
            if mid + l + r >= 2:
                res = node
            return mid or l or r
        helper(root)
        return res
