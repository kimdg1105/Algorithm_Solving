from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        for idx, num in enumerate(nums):
            v1 = 0
            for cnt, num2 in enumerate(nums[idx + 1 :]):
                idx2 = idx + 1 + cnt
                v1 = num - num2
                for cnt2, num3 in enumerate(nums[idx2 + 1 :]):
                    idx3 = idx2 + 1 + cnt
                    if idx < idx2 < idx3:
                        if result < v1 * num3:
                            result = v1 * num3
        return result


print(Solution().maximumTripletValue([12, 6, 1, 2, 7]))
print(Solution().maximumTripletValue([1, 10, 3, 4, 19]))
print(Solution().maximumTripletValue([2, 3, 1]))
