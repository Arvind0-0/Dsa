class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = []
        node = root
        while True:
            
            if node:
                queue.append(node)
                node = node.left
            elif queue:
                node = queue.pop()
                res.append(node.val)
                node = node.right
            else:
                break
                
            
        return res