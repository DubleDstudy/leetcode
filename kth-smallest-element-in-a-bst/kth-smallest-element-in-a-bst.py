# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        temp = root
        while k:
            while temp:
                stack.append(temp)
                temp = temp.left
            node = stack.pop()
            temp = node.right
            k -= 1
        return node.val
        