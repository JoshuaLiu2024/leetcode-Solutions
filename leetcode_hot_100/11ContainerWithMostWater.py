class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_volumn = 0

        while left < right :
            if height[left] <= height[right]:
                smaller = height[left]
            else:
                smaller = height[right]

            volumn_temp = (right - left) * smaller
            max_volumn = max(max_volumn,volumn_temp)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_volumn