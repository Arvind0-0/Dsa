class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:											
        c = Counter(words)                                   
        ans = sorted(c, key = lambda x: (-c[x],x)) 
        return ans[:k]  