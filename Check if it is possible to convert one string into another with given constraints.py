class Solution:
    def isItPossible(sef, S, T, M, N):
        #code here
        a1=[]
        a2=[]
        for a in S:
            if(a!="#"):
                a1.append(a)
        for a in T:
            if(a!="#"):
                a2.append(a)
        if(a1==a2):
            return 1
        else:
            return 0
