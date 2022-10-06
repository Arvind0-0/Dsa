class Solution:

    def lexicographicallySmallest (self, S, k):

        ans=""

        l=len(S)

        if (l&(l-1)):

            k+=k

        else:

            k//=2

        if k>=l:

            return "-1"

        st=[]

        for i in range(l):

            while st and k>0 and st[-1]>S[i]:

                st.pop()

                k-=1

            st.append(S[i])

        if k>0:

            while k>0:

                st.pop()

                k-=1

        while st:

            ans=st[-1]+ans

            st.pop()

        return ans

