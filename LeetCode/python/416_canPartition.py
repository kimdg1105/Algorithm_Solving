from collections import defaultdict
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        answer = False
        dp = defaultdict(list)
        n = len(nums)
        nums.sort()

        l, r = nums[:1], nums[1:]
        dp[0] = [l, r]
        print(dp)

        for i in range(1, n):
            cur_l = dp[i - 1][0].copy()
            cur_r = dp[i - 1][1].copy()
            for r_num in cur_r:
                new_l = cur_l.copy()
                new_r = cur_r.copy()
                new_l.append(r_num)
                new_r.remove(r_num)
                dp[i].append([new_l, new_r])

        print(dp)

        return answer


print(Solution().canPartition([1, 5, 11, 5]))
