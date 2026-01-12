class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_list = list(nums_set)
        nums_list.sort()
        min_pos = 1
        for val in nums_list:
            if val <= 0 :
                continue
            elif val == min_pos :
                min_pos += 1
            else :
                break
        return min_pos