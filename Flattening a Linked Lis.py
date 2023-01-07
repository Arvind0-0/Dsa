class Solution():
    def merge(self,l1,l2):
        if not l1 :
            return l2
        if not l2:
            return l1
        head=Node(-1)
        tmp=head
        while l1!=None and l2!=None:
            if l1.data<=l2.data:
                tmp.bottom=l1
                l1=l1.bottom
            else:
                tmp.bottom=l2
                l2=l2.bottom
            tmp=tmp.bottom
        if l1!=None:
            tmp.bottom=l1
        if l2!=None:
            tmp.bottom=l2
        return head.bottom
            
                
    
    def flatten(self,root):
        #Your code here
        while root.next!=None:
            a=root
            b=root.next
            c=root.next.next
            root=self.merge(a,b)
            root.next=c
        return root
