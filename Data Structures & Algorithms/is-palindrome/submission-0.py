class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        sen = []
        for c in s:
            if c.isalnum():
                sen.append(c.lower())
        
        left, right = 0, len(sen)-1
        while left < right:
            if sen[left] == sen[right]:
                left += 1
                right -=1 
            else:
                return False
        return True