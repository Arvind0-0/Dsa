class Solution:

    def median(self, matrix, R, C):

     #code here 

        import numpy as np

        

        m = np.array(matrix)

        ar = m.flatten()

        ar.sort()

        mid = (R*C)//2

 

        return ar[mid]
