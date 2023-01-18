class Solution:

    #Function to find first node if the linked list has a loop.

    def findFirstNode(self, head):

        #code here

        slow=head

        fast=head

        temp=head

        

        if(head is None or head.next is None):

            return -1

        

        while(fast.next is not None and fast.next.next is not None):

            slow=slow.next

            fast=fast.next.next

            if(fast==slow):

                while(slow!=temp):

                    slow=slow.next

                    temp=temp.next

                return temp.data

        return -1
