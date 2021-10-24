# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.index = 0
        
        def dfs(inorder_temp, preorder_temp, low, high):
            if low > high:
                return None            
            node = TreeNode(preorder_temp[self.index])
            inorder = inorder_temp.index(preorder_temp[self.index])
            self.index += 1
            node.left = dfs(inorder_temp, preorder_temp, low, inorder - 1)
            node.right = dfs(inorder_temp, preorder_temp, inorder + 1, high)
            return node
            
        return dfs(inorder, preorder, 0, len(inorder) - 1)