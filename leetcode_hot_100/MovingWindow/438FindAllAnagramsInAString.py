class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        result = []

        p_count = [0] * 26
        window_count = [0] * 26
        a = ord('a')

        for char in p:
            p_count[ord(char) - a] += 1

        for i, char in enumerate(s):
            window_count[ord(char) - a] += 1
            # 窗口长度维护
            if i >= len(p):
                left_char = s[i - len(p)]
                window_count[ord(left_char) - a] -= 1
            
            # 判断是否为异位词
            if i >= len(p) - 1 and window_count == p_count:
                result.append(i - len(p) + 1)
        return result