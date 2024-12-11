from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict = {}
        ans = 0
        for num in nums:
            dict[num] = True

        for num in nums:
            if num - 1 not in dict:
                cnt = 1
                target = num + 1
                while target in dict:
                    target += 1
                    cnt += 1
                ans = max(ans, cnt)

        return ans

