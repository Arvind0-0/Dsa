import bisect
class Solution:
    def getPairsCount(self, arr, n, k):
        arr.sort()
        x, c=0, 0
        for i in range(n-1):
            x = k-arr[i]
            y = bisect.bisect_left(arr,x,i+1,n)
            z = bisect.bisect(arr,x,i+1,n)
            c = c+z-y
        return c


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