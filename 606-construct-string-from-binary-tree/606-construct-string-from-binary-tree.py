class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # Initialising string with root.val
        string = str(root.val)
        # If root has a non-empty left subtree
        if root.left: 
            # we traverse it and wrap everything it returns in ()
            string += "(" + self.tree2str(root.left) + ")"
        # If root has a non-empty right subtree
        if root.right: 
            # If left subtree of root is empty, if we don't add empty () before actual
            # content of right subtree we can't differentiate whether it is from left
            # of right subtree. So, we are adding empty ()
            # Why we don't do like this in left subtree is, consider
            #   1
            # 2
            # Where 2 is left subtree of 1, "1(2)" and "1(2())" doesn't add any new
            # info to identify the tree
            # But, if the tree is like
            #   1
            #     2
            # Where 2 is right subtree of 1, "1(2)" and "1(()(2))" are different. 
            # Because "1(2)" won't tell that 2 is right child of 1.
            if not root.left: string += "()"
            # we traverse right subtree it and wrap everything it returns in ()
            string += "(" + self.tree2str(root.right) + ")"
        # Return string 
        return string