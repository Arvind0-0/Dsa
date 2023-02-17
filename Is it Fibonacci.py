class Solution():

    def solve(self, N, K, GeekNum):

        #your code goes here

        l=len(GeekNum)

        i=l

        while i<N:

            b=sum(GeekNum[i-K:i])

            GeekNum.append(b)

                

            i+=1

        return GeekNum[N-1]
