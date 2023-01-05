def longestString(self, arr, n):
        #your code goes here
        hash=set(arr)
        res=""
        for i in range(len(arr)):
            have=True
            for j in range(len(arr[i])):
                if arr[i][0:j+1] not in hash:
                    have=False
                    break
            if have:
                if len(res)<len(arr[i]):
                    res=arr[i]
                elif len(res)==len(arr[i]):
                    if arr[i]<res:
                        res=arr[i]
                        
        return res
