from typing import List

class Solution:

    def minCost(self, costs: List[List[int]]) -> int:

        # your code goes here

        N = len(costs)

        K = len(costs[0])

        if K == 1 and N>1:

            return -1

        if K==1 and N==1:

            return costs[0][0]

        rem = [0 for i in range(K)]

        min1 = [10 ** 7, 0]

        for j in range(K):

            rem[j] = costs[0][j]

            if min1[0] > rem[j]:

                min1[0] = rem[j]

                min1[1] = j

        min2 = 10 ** 7

        for j in range(K):

            if j == min1[1]:

                continue

            else:

                if min2 > rem[j]:

                    min2 = rem[j]

 

        for i in range(1, N):

            for j in range(K):

                if j == min1[1]:

                    rem[j] = costs[i][j] + min2

                else:

                    rem[j] = costs[i][j] + min1[0]

            min1 = [10 ** 7, 0]

            min2 = 10 ** 7

            for j in range(K):

                if min1[0] > rem[j]:

                    min1[0] = rem[j]

                    min1[1] = j

            for j in range(K):

                if j == min1[1]:

                    continue

                else:

                    if min2 > rem[j]:

                        min2 = rem[j]

        return min1[0]

