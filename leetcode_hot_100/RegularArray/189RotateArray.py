class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0 :
            return None
        
        k = k % n # 处理k>n的情况

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - k - 1)
        reverse(n - k, n - 1)
        reverse(0, n - 1)