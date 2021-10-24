# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        temp = [root]
        prv = TreeNode(left=root)

        while temp:
            curr = temp.pop()

            prv.left = None
            prv.right = curr

            if curr.right:
                temp.append(curr.right)
            if curr.left:
                temp.append(curr.left)

            prv = curr