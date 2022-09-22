class Solution:
    def max_of_subarrays(self,arr,n,k):

        if k==n:

            return [max(arr)]

        l=[]

        maxi=arr[0]

        maxid=0

        for i in range(k):

             if maxi<arr[i]:

                    maxi=arr[i]

                    maxid=i

        l.append(maxi)

        for i in range(k,n):

            if maxid<i-k+1:

                maxi=arr[maxid+1]

                maxid+=1

                for j in range(maxid+1,i+1):

                    if maxi<arr[j]:

                        maxi=arr[j]

                        maxid=j

                l.append(maxi)

                continue

            if maxi<arr[i]:

                maxi=arr[i]

                maxid=i

            l.append(maxi)

        return l
        
