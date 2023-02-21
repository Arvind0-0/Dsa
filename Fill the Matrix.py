def minIteration(self, N, M, x, y):

        #code here

        return max(max(x+y-2,y+N-1-x),max(x+M-y-1,N-x+M-y))
