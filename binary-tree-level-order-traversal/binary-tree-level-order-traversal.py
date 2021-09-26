# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if not root: return []
        q, ans = deque([root]), []
        
        while q:
            cnt = []
            for i in range(len(q)):
                temp = q.popleft()
                cnt.append(temp.val)
                if temp.left:  q.append(temp.left)
                if temp.right: q.append(temp.right)
            ans.append(cnt)
        return ans