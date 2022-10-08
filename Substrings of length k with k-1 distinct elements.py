#User function Template for python3

class Solution:
    def countOfSubstrings(self, S, K):
        ma={}
        coun=0
        for k in range(K):
            if(S[k] in ma):
                ma[S[k]]+=1
            else:
                ma[S[k]]=1
        ans=0
        if(len(ma)==K-1):
            ans=ans+1
        i=K
        j=0
        while(i<=len(S)-1):
            i=i+1
            j=j+1
            t_r=S[j-1]
            t_a=S[i-1]
            ma[t_r]-=1
            if(ma[t_r]==0):
                del ma[t_r]
            if(t_a not in ma):
                ma[t_a]=1
            else:
                ma[t_a]+=1
            if(len(ma)==K-1):
                ans+=1
            return ans
