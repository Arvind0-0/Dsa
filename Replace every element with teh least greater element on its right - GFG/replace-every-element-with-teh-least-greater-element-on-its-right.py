from typing import List
import bisect
class Solution:
    def findLeastGreater(self, n : int, a : List[int]) -> List[int]:
        ans = [-1]
        temp = [a[n-1]]
        for i in range(n-2,-1,-1):
            k = bisect.bisect_right(temp,a[i])
            if k>=0 and k<len(temp):
                bisect.insort_left(temp,a[i])
                ans.append(temp[k+1])
            else:
                bisect.insort_left(temp,a[i])
                ans.append(-1)
        return ans[::-1]

#{ 
 # Driver Code Starts


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findLeastGreater(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends