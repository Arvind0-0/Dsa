class Solution:
    def checkIfPangram(self, s: str) -> bool:
        i = 0   
        a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        count = 0
        for i in a:
            if i not  in s:
                return False
        return True
            
                    
                