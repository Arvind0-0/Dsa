class alphanumeric:
    def __init__(self,name,count):
        self.name=name
        self.count=count
class Solution:
    def sortedStrings(self,N,A):
        m={}
        for e in A:
            if e not in m:
                m[e]=0
            m[e]+=1
        b=set(A)
        c=list(b)
        c.sort()
        return [alphanumeric(x,m[x]) for x in c]
