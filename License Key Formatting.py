class Solution():
    def ReFormatString(self,S, K):
        s=''.join(S.split('-'))
        s=s.upper()
        s=s[::-1]
        ans=''
        l=[]
        for i in range(0,len(s),K):
            ans=ans+s[i:i+K]+'-'
        return ans[-2::-1]
