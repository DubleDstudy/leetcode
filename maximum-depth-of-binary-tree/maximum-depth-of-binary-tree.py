from collections import deque

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 0

        q = deque([root])
        while q:
            depth += 1
            for _ in range(len(q)):
                cur= q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return depth