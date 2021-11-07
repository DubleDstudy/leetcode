class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(1,len(height)):
            if height[i-1] > height[i]:
                stack.append((height[i-1], i-1))
            if height[i-1] < height[i]:
                cur = i-1
                while stack:
                    if stack[-1][0] <= height[i]:
                        temp, index = stack.pop()
                        ans += (min(height[i],temp)-height[cur])*(i-index-1)
                        cur = index 
                    else:
                        temp, index = stack[-1]
                        ans += (min(height[i],temp)-height[cur])*(i-index-1)
                        break
        return ans
        