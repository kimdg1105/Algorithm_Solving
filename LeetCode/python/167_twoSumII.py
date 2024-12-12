from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for idx, value in enumerate(numbers):
            needed = target - value
            if needed in dict:
                return [dict[needed] + 1, idx + 1]
            dict[value] = idx
