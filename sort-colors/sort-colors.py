class Solution:
    def sortColors(self, nums: List[int]) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            start, mid, end = 0, 0, len(nums)
            while mid < end:
                if nums[mid] < 1:
                    nums[start], nums[mid] = nums[mid], nums[start]
                    mid += 1
                    start += 1
                elif nums[mid] > 1:
                    end -= 1
                    nums[mid], nums[end] = nums[end], nums[mid]
                else:
                    mid += 1