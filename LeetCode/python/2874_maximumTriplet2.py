from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        length = len(nums)
        lmax = [0] * length
        rmax = [nums[length - 1]] * length

        for i in range(1, length - 1):
            lmax[i] = max(lmax[i - 1], nums[i - 1])
            rmax[length - 1 - i] = max(rmax[length - i], nums[length - i])

        for i in range(1, length):
            result = max(result, (lmax[i] - nums[i]) * rmax[i])

        return result


print(Solution().maximumTripletValue([12, 6, 1, 2, 7]))
print(Solution().maximumTripletValue([1, 10, 3, 4, 19]))
print(Solution().maximumTripletValue([2, 3, 1]))
print(Solution().maximumTripletValue([10, 13, 6, 2]))
