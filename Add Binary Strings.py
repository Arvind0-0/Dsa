class Solution:
    def addBinary(self, A, B):
        while A and A[0]=='0':
            A=A[1:]
        while B and B[0]=='0':
            B=B[1:]
        
        res=""
        carry, i, j=0, len(A)-1, len(B)-1

        while i>=0 or j>=0 or carry>0:
            x=int(A[i]) if i>=0 else 0
            y=int(B[j]) if j>=0 else 0
            v=x+y+carry
            carry=v//2
            v%=2
            res+=str(v)
            i,j=i-1, j-1
        return res[: :-1]
