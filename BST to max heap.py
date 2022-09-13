def convertToMaxHeapUtil(self, root):
        x,i = [],-1
        def ino(r):
            if not r:
                return
            ino(r.left)
            x.append(r.data)
            ino(r.right)
        
        
        def post(r):
            nonlocal i
            if not r:
                return
            post(r.left)
            post(r.right)
            i+=1
            r.data = x[i]
         
        ino(root)
        post(root)
