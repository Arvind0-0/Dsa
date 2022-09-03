class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        numset = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for i in range(n - 1):
            res = []
            for num in numset:
                cur = num % 10
                
                if cur + k <= 9: res.append(num * 10 + cur + k)
                if k != 0 and cur - k >= 0: res.append(num * 10 + cur - k)
                    
            numset = res
        
        return res