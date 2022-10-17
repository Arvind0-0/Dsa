class Solution:
    def checkIfPangram(self, s: str) -> bool:
        if len(set(s)) == 26:
            return True
        return False
            
                    
                