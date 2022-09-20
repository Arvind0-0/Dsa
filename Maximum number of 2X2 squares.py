class Solution:
    def numberOfSquares(self, base):
        noSquare = (base - 2) // 2
        return (noSquare * (noSquare + 1)) // 2
