class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = list()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right :
                sumup = nums[i] + nums[left] + nums[right]
                if sumup == 0:
                    results.append([nums[i],nums[left],nums[right]])
                    # 跳过重复的left和right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sumup > 0:
                    right -= 1
                else:
                    left += 1
            
        return results