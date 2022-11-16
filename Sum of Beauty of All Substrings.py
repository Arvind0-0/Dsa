class Solution:
    def beautySum(self, s):
        # Code here
        ans=0
        for i in range(len(s)):
            d={}
            for j in range(i,len(s)):
                if s[j] in d:
                    d[s[j]]+=1
                else:
                    d[s[j]]=1
                mf=max(d.values())
                lf=min(d.values())
                ans+=(mf-lf)
        return ans
