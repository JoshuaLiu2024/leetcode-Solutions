class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        
        need = defaultdict(int) # dict{字符：频率}，这是t中字符的频率
        window = defaultdict(int) # dict{字符：频率}，这是窗口中字符的出现频率

        for char in t:
            need[char] = need.get(char,0) + 1

        # 创建窗口
        left, right = 0, 0
        valid = 0 # 记录已经满足条件的字符的个数
        start = 0
        min_len = float('inf') # 记录最小包含t的字符串长度

        while right < len(s) :
            # 扩大右窗口，更新window
            char_1 = s[right]
            right += 1
            if char_1 in need :
                window[char_1] += 1
                if window[char_1] == need[char_1]:
                    valid += 1
            
            while valid == len(need):
                if right - left < min_len:
                    start = left
                    min_len = right - left

                # 缩小左窗口，更新window和min_len
                char_2 = s[left]
                left += 1
                if char_2 in need :
                    if window[char_2] == need[char_2]:
                        valid -= 1
                    window[char_2] -= 1
        
        return "" if min_len == float('inf') else s[start:start+min_len]