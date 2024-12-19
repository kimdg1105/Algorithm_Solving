from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bfs(self, root: Optional[TreeNode], visited: list[Optional[TreeNode]]):
        q = deque()

        q.append(root)

        while q:
            cur_node = q.popleft()
            if cur_node == None:
                visited.append(None)
            if cur_node in visited:
                continue
            else:
                visited.append(cur_node)

                q.append(cur_node.left)
                q.append(cur_node.right)

        return visited

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = True

        first_visited = self.bfs(p, [])
        second_vistied = self.bfs(q, [])

        first_val = []
        second_val = []
        for tree_node in first_visited:
            if tree_node == None:
                first_val.append(None)
            else:
                first_val.append(tree_node.val)
        for tree_node in second_vistied:
            if tree_node == None:
                second_val.append(None)
            else:
                second_val.append(tree_node.val)

        return first_val == second_val
