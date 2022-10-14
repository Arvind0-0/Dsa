class Solution:
    def maximizeSum (self,arr, n) : 
        s=set()
        d={}
        for i in range(n):
            s.add(arr[i])
            d[arr[i]]=d.get(arr[i],0)+1
        a=list(s)  
        m=len(a)
        ans=0
        for i in range(n-1,-1,-1):
            if d[arr[i]]:
                ans+=arr[i]
                d[arr[i]]-=1
                if arr[i]-1 in d:
                    if d[arr[i]-1]:
                        d[arr[i]-1]-=1
        for k,v in d.items():
            if v!=0:
                ans+=k*v
        return ans
