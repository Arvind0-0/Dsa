class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:                    
        n = len(nums)
        
        def partition(l, r, pivot):
            pivot_elem=nums[pivot]
            nums[r],nums[pivot]=nums[pivot],nums[r]
            
            index=l
            for i in range(l, r):
                if nums[i]<pivot_elem:
                    nums[i],nums[index]=nums[index],nums[i]
                    index+=1
            
            nums[index],nums[r]=nums[r],nums[index]
            return index
        
        def quick_select(l,r,kth_index):
            if l==r:
                return nums[l]
            
            pivot_index=partition(l,r,l)
            
            if pivot_index==kth_index:
                return nums[pivot_index]
            
            if kth_index>pivot_index:
                return quick_select(pivot_index+1, r, kth_index)
            else:
                return quick_select(l,pivot_index-1, kth_index)
        
        return quick_select(0, n - 1, n - k)
