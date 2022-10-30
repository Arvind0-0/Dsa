class Solution:
    def NoOfChicks(self, n):
        if n <= 1:
            return 1
        if n <= 6:
            return 3 * self.NoOfChicks(n-1)
        elif n == 7:
            return (3 * self.NoOfChicks(n-1) - 3 * self.NoOfChicks(n-6))
        else:
            return (3 * self.NoOfChicks(n-1) - 2 * self.NoOfChicks(n-6))
