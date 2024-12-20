# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, visited: list, lv, direct: Optional[str]) -> list:
        if root == None:
            visited.append(None)

        if root != None and root.val not in visited:
            lv += 1
            visited.append((root.val, lv))

            if direct == "l":
                self.dfs(root.left, visited, lv, "l")
                self.dfs(root.right, visited, lv, "l")
            if direct == "r":
                self.dfs(root.right, visited, lv, "r")
                self.dfs(root.left, visited, lv, "r")

        return visited

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l_visited = []
        r_visited = []

        if root == None:
            return False

        lv = 1
        l_visited.append((root.val, lv))
        r_visited.append((root.val, lv))

        l_visited = self.dfs(root.left, l_visited, lv, "l")
        r_visited = self.dfs(root.right, r_visited, lv, "r")

        print("l: ", l_visited)
        print("r: ", r_visited)

        return l_visited == r_visited
