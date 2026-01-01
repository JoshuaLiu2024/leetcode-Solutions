class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        length = len(nums)
        left_product = list()
        for idx in range(length):
            if idx == 0 :
                left_product.append(1)
            else :
                temp = left_product[-1] * nums[idx - 1]
                left_product.append(temp)
        
        right_product = [1] * length
        for idx in range(length-2, -1, -1):
            right_product[idx] = right_product[idx+1] * nums[idx+1]

        return [left_product[i] * right_product[i] for i in range(length)]