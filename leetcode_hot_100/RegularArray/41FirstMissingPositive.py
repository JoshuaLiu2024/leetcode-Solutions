class Solution_1:
    # Time: O(NlogN)
    # Space: O(N)
    # 这种方法比较直观，但是不符合题目要求的O(1)空间复杂度和O(N)时间复杂度。
    # 原理是利用set去重，然后排序，最后遍历找到第一个缺失的正整数。
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
    
class Solution_2:
    # 可以使用哈希表实现O(N)时间复杂度，但空间复杂度为O(N)的算法。
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        i = 1
        while True:
            if i not in num_set:
                return i
            i += 1

            
class Solution_3:
    # Time: O(N)
    # Space: O(1)
    # 这种方法符合题目要求的O(1)空间复杂度和O(N)时间复杂度。
    # 原理是将每个正整数放到它对应的索引位置上，例如数字1放在索引0的位置，数字2放在索引1的位置，依此类推。
    # 最后遍历数组，找到第一个索引位置不匹配的数字，即为缺失的最小正整数。
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1