# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        temp = head
        temp1 = head.next.next
        while temp1 and temp1.next:
            temp = temp.next
            temp1 = temp1.next.next
        temp.next = temp.next.next
        return head