class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		nums1[m:m+n]=nums2
		nums1.sort()