class Solution:
    def insert_node(self, root, depth):
        if root is None:
            return None
        if depth == self.depth-1:
            l = root.left
            r = root.right

            new_left = TreeNode(self.val)
            new_right = TreeNode(self.val)

            new_left.left = l
            new_right.right = r

            root.left = new_left
            root.right = new_right
            
        self.insert_node(root.left, depth+1)
        self.insert_node(root.right,depth+1)
        return root

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.depth = depth
        self.val = val
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            root = new_root
        else:
            root = self.insert_node(root,1)
        return root