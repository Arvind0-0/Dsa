class Solution:

    def minIncrements(self, arr, N): 

        # Code here

        increment=0

        arr.sort()

        for i in range(1,N):

            if arr[i]<=arr[i-1]:

                while arr[i]<=arr[i-1]:

                    increment+=1

                    arr[i]+=1

        return increment
