from bisect import bisect_left
class Solution:
    def removeStudents(self, H, N):
        # code here
        ans=[H[0]]
        for i in range(1, N):
            if H[i]>ans[-1]:
                ans.append(H[i])
            else:
                ans[bisect_left(ans, H[i])]=H[i]
        return N-len(ans)
