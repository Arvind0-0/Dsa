class Solution:
    def leftSmaller(self, n, a):
        ans=[-1]*n
        st=[]
        for i in range(len(a)):
            while st and a[st[-1]]>=a[i]:
                st.pop()
            if st:
                ans[i]=a[st[-1]]
            st.append(i)
        return ans
