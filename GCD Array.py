from typing import List

class Solution:

    def solve(self, N : int, K : int, arr : List[int]) -> int:

        # code here

        a = sum(arr)

        d = []

        m = int(a ** 0.5)

        for i in range(1, m+1):

            if a % i == 0:

                d.append(i)

                if i != (a // i):

                    d.append(a // i)

        

        d.sort(reverse = True)

        for i in range(1, N):

            arr[i] += arr[i-1]

        

        out = 1

        for x in d:

            cnt = 0

            for y in arr:

                if (y % x == 0):

                    cnt += 1

            

            if cnt >= K:

                out = x

                break

        

        return out
