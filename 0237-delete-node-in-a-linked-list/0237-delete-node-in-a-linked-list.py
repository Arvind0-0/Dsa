class Solution:
    def deleteNode(self, node:ListNode):
        node.val  = node.next.val
        node.next = node.next.next
        return