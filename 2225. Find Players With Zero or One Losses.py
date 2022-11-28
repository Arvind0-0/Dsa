class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players = set(chain(*matches))                  
        loses = Counter([y for _,y in matches])         
        zeros = [p for p in players if loses[p] == 0]  
        ones  = [p for p in players if loses[p] == 1]   
        return [sorted(zeros), sorted(ones)]  
