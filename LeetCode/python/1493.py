from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        arr = [0] * len(nums)

        arr[0] = nums[0]
        for idx, val in enumerate(nums[1:]):
            if val == 1:
                arr[idx] += arr[idx - 1] + 1
            else:
                if idx != len(nums) - 1 and nums[idx + 1] == 1:
                    arr[idx] = arr[idx - 2] + 1

        print(arr)
        return 0


print(Solution().longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
