class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if  head and head.next:
            self.swapPairs(head.next.next)
            head.val, head.next.val=head.next.val,head.val
        return head
