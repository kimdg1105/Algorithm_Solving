from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        ans = 0

        max_value = 0
        for idx, value in enumerate(arr):
            max_value = max(max_value, value)
            if max_value == idx:
                ans += 1

        return ans


sol = Solution()
print(sol.maxChunksToSorted([4, 3, 2, 1, 0]))  # 1
print(sol.maxChunksToSorted([1, 0, 2, 3, 4]))  # 4
print(sol.maxChunksToSorted([2, 0, 1]))  # 1
print(sol.maxChunksToSorted([1, 2, 0, 3]))  # 2
