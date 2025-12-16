class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_groups = dict()

        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagrams_groups:
                anagrams_groups[key] = []
            anagrams_groups[key].append(s)

        return list(anagrams_groups.values())    