from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
        
        for  num, idx in sorted_nums:
            if nums[idx] != False:
                score += nums[idx]
                nums[idx] = False
                if idx > 0:
                    nums[idx-1] = False
                if idx < len(nums) -1:
                    nums[idx+1] = False        
        return score

sol = Solution()
print(sol.findScore([2,1,3,4,5,2]))
print(sol.findScore([2,3,5,1,3,2]))
