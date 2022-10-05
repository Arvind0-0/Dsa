class Solution:

    def prefixCount(self, N, Q, li, query):

        # code here

        d={}

        for i in li:

            s=""

            for j in i[0]:

                s+=j

                if s in d:

                    d[s]+=1

                else:

                    d[s]=1

        m=[]

        for i in query:

            if i[0] in d:

                m.append(d[i[0]])

            else:

                m.append(0)

        return m
