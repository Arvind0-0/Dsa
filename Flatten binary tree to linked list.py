class Solution:

    prev=None

    def flatten(self, root):

        #code here

        if root is None:

            return

        self.flatten(root.right)

        self.flatten(root.left)

        root.left = None

        root.right = self.prev

 

        self.prev = root
