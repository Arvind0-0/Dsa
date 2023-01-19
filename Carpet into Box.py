class Solution:
    def carpetBox(self, a,b,c,d):
        a,b = min(a,b),max(a,b)
        c,d = min(c,d),max(c,d)
        if (a <= c and b <= d) or (a <= d and b <= c):
            return 0
        if (a > c and b <= d):
            return 1 + self.carpetBox(a//2,b,c,d)
        else:
            return 1 + self.carpetBox(a,b//2,c,d)
