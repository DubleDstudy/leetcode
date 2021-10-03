# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [(root,0)]
        temp = dict()
        while q:
            node,level = q.pop(0)
            temp[level] = node.val
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
        ans = []
        for k in temp.keys():
            ans.append(temp[k])
        return ans