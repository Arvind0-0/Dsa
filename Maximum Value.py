from collections import deque
class Solution:
    def maximumValue(self, node):
        if not node: return
    
        q = deque([node])
        res = []
        
        while q:
            
            temp = 0
            
            for _ in range(len(q)):
                root = q.popleft()
                temp = max(temp, root.data)
                
                if root.left: q.append(root.left)
                if root.right: q.append(root.right)
                
                
            res.append(temp)
            
        return res
