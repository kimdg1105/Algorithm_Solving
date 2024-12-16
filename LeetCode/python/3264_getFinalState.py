from heapq import heappop, heappush
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heapq = []

        for idx, num in enumerate(nums):
            heappush(heapq, (num, idx))

        while k != 0:
            print(nums)
            min_num, min_idx = heappop(heapq)
            min_num = min_num * multiplier * 1
            nums[min_idx] = min_num
            heappush(heapq, (min_num, min_idx))
            k -= 1

        return nums


sol = Solution()
print(sol.getFinalState([2, 1, 3, 5, 6], 5, 2))
