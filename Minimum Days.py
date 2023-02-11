class Solution:
    def getMinimumDays(self, n : int, s : str, p : List[int]) -> int:
        s = list(s)
        day = 0
        for i in range(n-1):
            
            if s[i] != "?" and s[i] == s[i+1]:
                while s[i] == s[i+1]:
                    s[p[day]] = "?"
                    day += 1
        return day
