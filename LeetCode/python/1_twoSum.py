from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx, value in enumerate(nums):
            needed = target - value
            if needed in dict:
                return [dict[needed], idx]
            dict[value] = idx
