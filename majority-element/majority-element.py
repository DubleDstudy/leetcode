class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans= collections.Counter(nums).most_common()
        return ans[0][0]