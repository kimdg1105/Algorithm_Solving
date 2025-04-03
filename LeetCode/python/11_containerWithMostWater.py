from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        w = r - l
        h = min(height[l], height[r])

        ans = w * h

        while l != r:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            cur_ans = (r - l) * min(height[l], height[r])
            ans = max(ans, cur_ans)

        return ans


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
