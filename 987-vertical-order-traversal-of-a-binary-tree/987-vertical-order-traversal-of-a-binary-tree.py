from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_rows = defaultdict(list)

        queue = deque()
        queue.append((root, 0, 0))
        while queue:
            node_x_y = queue.popleft()
            node, x, y = node_x_y[0], node_x_y[1], node_x_y[2]
            col_rows[y].append((x, node.val))
            if node.left:
                queue.append((node.left, x + 1, y - 1))            
            if node.right:
                queue.append((node.right, x + 1, y + 1))

        rst = []
        min_col, max_col = min(col_rows.keys()), max(col_rows.keys())
        for col in range(min_col, max_col + 1):
            if col not in col_rows:
                continue
            col_rows[col].sort()
            rst.append([t[1] for t in col_rows[col]])
        return rst