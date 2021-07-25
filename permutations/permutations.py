import itertools  
class Solution:
   
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        for i in itertools.permutations(nums,len(nums)):
            ans.append(i)
        return ans
        