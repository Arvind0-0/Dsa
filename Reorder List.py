class Solution:
    def reorderList(self,head):
        if not head or not head.next: return

        slow, fast = head, head.next
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 1 2 3 4 5 6 7 8 9
        
        # Separate both lists until middle node
        second = slow.next
        slow.next = None
        
        # first list -- 1 2 3 4 5->null    second list -- 6 7 8 9->null
        
        # reverse the second list
        
        p = second
        q = r = None
        while p:
            r = q
            q = p
            p = p.next
            q.next = r
            
        first, second = head, q
        
        # 1 2 3 4 5->null 9 8 7 6->null
        
        # 1->9->2->8->3_7....
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
