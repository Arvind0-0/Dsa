class Solution:

    def findMaxSum(self,arr, n):

        for i in range(2,n):

            if i-3>=0:

                t=max(arr[i-2],arr[i-3])

            else:

                t=arr[i-2]

            arr[i]+=t

        return(max(arr[n-2:]))
