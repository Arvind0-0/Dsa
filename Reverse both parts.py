from typing import Optional
class Solution:
    def reverse(self, head : Optional['Node'], k : int) -> Optional['Node']:
        leng=0
        a=head
        while a:
            leng+=1
            a=a.next
        dummy=Node(-1)
        b=dummy
        for i in range(k):
            dummy.next=head
            head=head.next
            dummy=dummy.next
        dummy.next=None
    
        curr,prev=b.next,None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        b.next=prev
        
        dummy1=Node(-1)
        c=dummy1
        for i in range(leng-k):
            dummy1.next=head
            head=head.next
            dummy1=dummy1.next
        dummy1.next=None
    
        curr1,prev1=c.next,None
        while curr1:
            temp1=curr1.next
            curr1.next=prev1
            prev1=curr1
            curr1=temp1
        c.next=prev1
        
        dummy=Node(-1)
        res=dummy
        while prev:
            dummy.next=prev
            prev=prev.next
            dummy=dummy.next
        
        while prev1:
            dummy.next=prev1
            prev1=prev1.next
            dummy=dummy.next
            
        return res.next
