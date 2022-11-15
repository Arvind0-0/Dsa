class Solution:
    def longestPerfectPiece(self, arr, N):
        res = 0
        i = 0
        j = 0
        while (j < N):
            while(abs(arr[j] - arr[i]) > 1):
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res
