class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}":"{",
                    "]": "[",
                    ")":"("}
        stack = []
        for ch in s:
            if ch in brackets:
                if not stack:
                    return False
                elif stack.pop() != brackets[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack

        # Time: O(n) -- one pass over s, each stack op is O(1)
        # Space: O(n) -- worst case, stack holds all n opening brackets
