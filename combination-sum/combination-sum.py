class Solution():
    def combinationSum(self, candidates, target):
        ans = []
        self.dfs(candidates, target, [], ans)
        return ans
    
    def dfs(self, temp, target, cnt, ans):
        if target < 0:
            return 
        if target == 0:
            ans.append(cnt)
            return 
        for i in range(len(temp)):
            self.dfs(temp[i:], target-temp[i], cnt+[temp[i]], ans)