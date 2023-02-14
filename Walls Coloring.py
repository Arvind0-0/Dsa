class Solution():
    def minCost(self, colors, N):
        
        p=b=y=0
        for i in range(N):
            cp=min(b,y)+colors[i][0]
            cb=min(p,y)+colors[i][1]
            cy=min(p,b)+colors[i][2]
            p,b,y=cp,cb,cy
        return min(p,b,y)
