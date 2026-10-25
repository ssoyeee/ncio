from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            word_dict[key].append(s)
        return list(word_dict.values())