class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count= Counter(s)
        print(s_count)
        t_count = Counter(t)
        print(t_count)
        if s_count == t_count:
            return True
        return False