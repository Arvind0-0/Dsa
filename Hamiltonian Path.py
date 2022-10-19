class Solution:

    def check(self, N, M, Edges):

        # code here

        bool1 = False

        dict1 = defaultdict(set)

        for i in range(len(Edges)):

            dict1[Edges[i][0]].add(Edges[i][1])

            dict1[Edges[i][1]].add(Edges[i][0])

        for i in range(1, N + 1):

            set1 = set()

            set1=chkH(dict1, set1, i, N)

            if len(set1) == N:

                bool1 = True

                break

        return bool1
