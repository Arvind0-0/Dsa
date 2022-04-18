from typing import Generator
class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		for i, num in enumerate(self.helper(root),1):
			if i == k: return num

	def helper(self, root: Optional[TreeNode]) -> Generator:
		if root:
			yield from self.helper(root.left)
			yield root.val
			yield from self.helper(root.right)
