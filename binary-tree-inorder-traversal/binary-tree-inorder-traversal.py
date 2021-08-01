class Solution:
    def inorderTraversal(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            temp.append(node.val)
            dfs(node.right)
        
        temp = []
        dfs(root)
        return temp
