class Solution_1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 暴力解法
        longest = 0
        n = len(s)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                longest = max(longest, j - i + 1)
        return longest

class Solution_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动字典 + 哈希表
        window = dict()
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in window and window[char] >= left:
                left = window[char] + 1
            
            window[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len