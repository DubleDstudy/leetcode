class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = Counter(nums)
        return ans.most_common(1)[0][0]