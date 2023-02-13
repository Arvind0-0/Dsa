class Solution:
    def inSequence(self, A, B, C):
        if C==0: return 1 if A==B else 0
        n = (B+C-A)/C
        return 1 if n*10==int(n)*10 and n>0 else 0
