class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]

        for val in nums[1:]:
            current_sum = max(val, current_sum + val)
            max_sum = max(current_sum, max_sum)
        return max_sum