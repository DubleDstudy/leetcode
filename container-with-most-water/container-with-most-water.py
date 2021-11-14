class Solution:
    def maxArea(self, height: List[int]) -> int:

       
        start, end = 0, len(height)-1
               
        max_size = len(height) - 1
        
        ans = 0

        for width in range(max_size, 0, -1):
            
            if height[start] < height[end]:
              
                ans = max(ans, width * height[start] )
                start += 1            
            else:

                ans = max(ans, width * height[end] )
                end -= 1
                
        return ans