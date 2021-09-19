class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = nums[:k]
        heapq.heapify(temp)
        
        for i in range(k, len(nums)):
            if nums[i] > temp[0]:
                heapq.heappushpop(temp, nums[i])
        return temp[0]