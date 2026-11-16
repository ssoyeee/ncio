# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return []
        q = deque()
        q.append(root)

        while q:
            size = len(q)
            level = []
            for _ in range(size):
                x = q.popleft()
                level.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            result.append(level)
        return result
        
        # Time: O(n) -- each node added to the queue and removed once
        # Space: O(w) -- where w is max number of nodes in one level