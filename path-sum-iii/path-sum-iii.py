class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        def dfs(root, prevSum, sum):
            if not root:
                return 
            temp = prevSum + root.val
            if temp - sum in cnt:
                self.count += cnt[temp - sum]
            if temp in cnt:
                cnt[temp] += 1
            else:
                cnt[temp] = 1
            dfs(root.left, temp, sum)
            dfs(root.right, temp, sum)
            cnt[temp] -= 1
            
        self.count = 0
        cnt = {0:1}
        dfs(root, 0, sum)
        return self.count