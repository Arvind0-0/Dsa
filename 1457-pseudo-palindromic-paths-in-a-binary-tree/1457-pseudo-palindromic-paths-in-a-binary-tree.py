'''
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        
        def isPalid(path):
            md = set()
            for p in path:
                if p in md:
                    md.remove(p)
                else:
                    md.add(p)
            return True if len(md)<=1 else False
        
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                # res.append(path)
                if isPalid(path):
                    self.cnt += 1
            if root.left:
                dfs(root.left, path+[root.left.val])
            if root.right:
                dfs(root.right, path+[root.right.val])
                
        res = []
        dfs(root, [root.val])
                
        return self.cnt 
'''

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        
        def dfs(root, path):
            if root:
                path = path ^ (1 << root.val)
                if not root.left and not root.right:
                    if path & (path - 1) == 0:
                        self.cnt += 1
                else:
                    dfs(root.left, path)
                    dfs(root.right, path)
                    
        dfs(root, 0)
        
        return self.cnt