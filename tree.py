class Solution:

    def level(self,node):

        head=node

        q=[head,None]

        q1=[]

        m={}

        while(len(q)!=0):

            temp=q.pop(0)

            if temp==None:

                if len(q)==0:

                    q1.append(m)

                    break

                q1.append(m)

                q.append(None)

                m={}

                continue

            if temp.data in m:

                m[temp.data]+=1

            else:

                m[temp.data]=1

            # l.append(temp.data)

            if temp.left!=None:

                q.append(temp.left)

            if temp.right!=None:

                q.append(temp.right)

        return q1

    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:

        # code here

        x=self.level(node1)

        y=self.level(node2)

        # print(x)

        # print(y)

        if len(x)!=len(y):

            return 0

        for i in range(len(x)):

            for j in x[i]:

                if j not in y[i] or x[i][j]!=y[i][j]:

                    return 0

        return 1
