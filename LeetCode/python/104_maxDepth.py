# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0

        if root == None:
            return level
        
        q = deque()
        q.append((root, 1))

        while q :
            cur_node, cur_level = q.popleft()

            if cur_node.left != None:
                q.append((cur_node.left,cur_level+1))
            if cur_node.right != None:
                q.append((cur_node.right, cur_level+1))
            level = max(level, cur_level)
        
        return level
    

sol = Solution()
sol.maxDepth()