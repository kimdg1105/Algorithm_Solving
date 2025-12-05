from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans = original
        if ans in nums:
            ans = Solution().findFinalValue(nums, 2 * ans)
        return ans


print(Solution().findFinalValue([5, 3, 6, 1, 12], 3))
