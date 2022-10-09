class Solution:
    def __init__(self):
        self.recode = dict()
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:return False
        
        if k-root.val in self.recode: return True
        
        self.recode[root.val]=None 
        
        return self.findTarget(root.left,k) or self.findTarget(root.right,k)