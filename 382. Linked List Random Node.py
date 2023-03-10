class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.res = []
        
        while head:
            self.res.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return random.choice(self.res)
