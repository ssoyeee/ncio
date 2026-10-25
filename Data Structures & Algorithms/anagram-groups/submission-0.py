class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_count = {}
        output = []

        for word in strs:
            key = "".join(sorted(word))
            if key in strs_count:
                strs_count[key].append(word)
            else:
                strs_count[key] = []
                strs_count[key].append(word)
        
        output = list(strs_count.values())

        return output    
