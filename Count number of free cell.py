class Solution():
    def countZero(self, n, k ,arr):
        #your code here
        r,c=0,0
        ans=[]
        s1,s2=set(),set()
        for i in arr:
            if i[0] not in s1:
                s1.add(i[0])
                r+=1
            if i[1] not in s2:
                s2.add(i[1])
                c+=1
            ans.append(n*n-((n*r)+(n*c)-(r*c)))
       
        
        return ans
