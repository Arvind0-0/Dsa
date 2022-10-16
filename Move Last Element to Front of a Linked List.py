from typing import Optional
class Solution:
    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
        if head is None or head.next is None:
            return head
        temp = head
        while temp.next.next is not None:
            temp = temp.next
        end = temp.next
        temp.next = None
        end.next = head
        head = end 
        return head
