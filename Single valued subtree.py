class Solution:

    def singlevalued(self, root):

        #code here

        count=[0]

        def value(root):

            if not root:

                return 0,True

            if not root.left and not root.right:

                count[0]+=1

                return root.data,True

            data1,boo1=value(root.left)

            data2,boo2=value(root.right)

            if ((root.data==data1 and root.data==data2) or ((data1==0 and root.data==data2) or (root.data==data1 and data2==0))) and (boo1 and boo2):

                count[0]+=1

                return root.data,boo1 and boo2

            else:

                return -1,False

        v,v1=value(root)

        return count[0]
