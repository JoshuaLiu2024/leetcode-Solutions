class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和 + 哈希表
        presum = 0
        index = 0
        premap = {0:1}

        for num in nums:
            presum += num

            if presum - k in premap:
                index += premap[presum - k]
            premap[presum] = premap.get(presum, 0) + 1
        return index