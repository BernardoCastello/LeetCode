class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        max_water = 0
        left = 0
        right = len(height) -1

        while left < right:
            m = min(height[left],height[right])

            water = (right - left) * m
            if water > max_water:
                max_water = water
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
    
S = Solution()

print(S.maxArea([1,8,6,2,5,4,8,3,7]))