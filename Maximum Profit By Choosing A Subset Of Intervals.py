from typing import List

def search(arr,ele):
    l = 0
    ans = len(arr)
    h = len(arr)-1
    while l<=h:
        mid =  (l+h)//2
        if arr[mid][0]<ele:
            l = mid+1
        else:
            h = mid-1
            ans = min(ans,mid)
    return ans
class Solution:
    def maximum_profit(self, n : int, intervals : List[List[int]]) -> int:
        # code here
        intervals.sort(key = lambda x:x[0] )
        dp = [0]*n
        for i in range(n-1,-1,-1):
            ind = search(intervals,intervals[i][1])
            if ind>=n:
                dp[i] = intervals[i][2]
            else:
                dp[i] = (intervals[i][2]+dp[ind])
            
            if i!=n-1:
                dp[i] = max(dp[i],dp[i+1])
        return dp[0]
