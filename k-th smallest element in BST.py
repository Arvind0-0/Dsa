class Solution:

    def inorder(self,root):

        if root:

            self.inorder(root.left)

            self.k-=1

            if self.k==0:

                self.ans=root.data

                return 

            self.inorder(root.right)

            

    def KthSmallestElement(self, root, k):

        self.k=k

        self.ans=None

        self.inorder(root)

        if self.ans!=None:

            return self.ans

        return -1    
