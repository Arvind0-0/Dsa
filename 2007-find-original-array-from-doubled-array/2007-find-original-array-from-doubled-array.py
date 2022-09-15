
class Solution:
    def findOriginalArray(self, nums: List[int]) -> List[int]:
            ans = [] 
            vacans = [] 
            if len(nums)%2:
                    return ans  
            nums.sort()
			#sorting 

            temp = Counter(nums)
			#storing the frequencies
            for i in nums:    
                if temp[i] == 0:       
                    continue
                else:
                    if temp.get(2*i,0) >= 1:
                        ans.append(i)
                        temp[2*i] -= 1
                        temp[i] -= 1
                    else:        
                        return vacans
            return ans