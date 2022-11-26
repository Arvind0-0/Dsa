class Solution:

    def treeFromString(self, s : str) -> Optional['Node']:

        # code here

        q = [Node('')]

        for i in s : 

            if i == '(' :

                new = Node('')

                if q[-1].left == None :

                    q[-1].left = new

                else : 

                    q[-1].right = new

                q.append(new)

            elif i == ')' :

                q.pop()

            else : 

                q[-1].data += i

        return q[0]
