class Solution:
    def subsets(self, nums):
        nums.sort() 
        ans = []
        for i in range(len(nums) + 1):
            temp = itertools.combinations(nums, i)
            for comb in temp:
                ans.append(list(comb))
        return ans 