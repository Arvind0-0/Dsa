class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n=len(words)                        
        char_set = [set(words[i]) for i in range(n)] # precompute hashset for each word                                                  
        max_val = 0
        for i in range(n):
            for j in range(i+1, n):
                if not (char_set[i] & char_set[j]): # if nothing common
                    max_val=max(max_val, len(words[i]) * len(words[j]))
        
        return max_val   
