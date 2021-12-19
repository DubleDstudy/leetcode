# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        temp = deque([(root.left, root.right)])
        while temp:
            le, ri = temp.pop()
            if le is None and ri is None:
                continue
            if le is None or ri is None:
                return False
            if le.val != ri.val:
                return False
            temp.append((le.left, ri.right))
            temp.append((le.right, ri.left))
        return True
        