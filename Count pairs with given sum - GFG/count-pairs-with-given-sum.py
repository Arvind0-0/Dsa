from collections import defaultdict
class Solution:
    def getPairsCount(self, arr, n, k):
        count=0
        d=defaultdict(int)
        for i in arr:
            if (k-i in d):
                count+=d[k-i]
            d[i]+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends