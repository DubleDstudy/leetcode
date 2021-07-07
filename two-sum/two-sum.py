class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       ans = {}
       for i, v in enumerate(nums): #1
           temp = target - nums[i] #2
           
           if temp in ans: #3
               return [i, ans[temp]]  #4
           else:
               ans[v] = i  #5