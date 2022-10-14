class Solution:
    def containsDuplicate(self, arr: List[int]) -> bool:
        arr.sort()
        i=0
        for i in range(len(arr)-1):
            if arr[i]!=arr[i+1]:
                i+=1
                continue
            else:
                return True
            return False