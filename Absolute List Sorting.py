class Node:

    def __init__(self, data):   # data -> value stored in node

        self.data = data

        self.next = None

 

class Solution:

    

    def sortList(self,head):

        neg=(-1)

        neg_last=neg

        pos=Node(1)

        pos_last=pos

        c=0

        while head:

            

            if head.data<0:

                temp=head

                head=head.next   

                temp.next=neg

                neg=temp

                if c==0:

                    neg_last=temp

                    c+=1

            else:

               temp=head

               head=head.next

               temp.next=None

               pos_last.next=temp

               pos_last=pos_last.next

        if c!=0:

            neg_last.next=pos.next

            return neg

        else:

            return pos.next
