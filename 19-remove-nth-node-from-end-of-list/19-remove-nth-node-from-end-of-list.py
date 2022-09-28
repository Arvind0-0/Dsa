class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        currentHeader = head
		# 1. Count LinkedListLength
        while currentHeader != None:
            length += 1
            currentHeader = currentHeader.next
        currentHeader = head
		# 2. return next node if n == length
        if n == length: return head.next
        removeNextCounter = length - n
		# 3. Find the item before the removed item and set to item after the removed one
        while currentHeader != None:
            removeNextCounter -= 1
            if removeNextCounter == 0:
                currentHeader.next = currentHeader.next.next
                break
            currentHeader = currentHeader.next
        return head