from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = 0
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
