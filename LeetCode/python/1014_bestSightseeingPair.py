from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        cur = values[0]
        for i in range(1, len(values)):
            ans = max(ans, cur + values[i] - i)
            cur = max(cur, values[i] + i)

        return ans


print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]))
