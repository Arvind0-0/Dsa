class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res: list[str] = ["."] * len(dominoes)
        rightmost_right = -2
        rightmost_left = -1

        for i, d in enumerate(dominoes):
            if d == "R":
                if rightmost_right > rightmost_left:
                    for di in range(rightmost_right+1, i):
                        res[di] = "R"
                
                rightmost_right = i
                res[i] = "R"
            elif d == "L":
                if rightmost_left > rightmost_right:
                    for di in range(rightmost_left+1, i):
                        res[di] = "L"
                else:
                    for delta in range(1, (i - rightmost_right + 1) // 2):
                        res[rightmost_right + delta] = "R"
                        res[i - delta] = "L"
                rightmost_left = i
                res[i] = "L"
        
        if rightmost_right > rightmost_left:
            for di in range(rightmost_right+1, i+1):
                res[di] = "R"
        
        return "".join(res)