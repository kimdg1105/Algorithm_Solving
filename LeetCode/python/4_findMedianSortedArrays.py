from typing import List


class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		merger_list = nums1 + nums2
		merger_list.sort()
		length = len(merger_list)

		if length % 2 != 0:
			return merger_list[length // 2]
		else:
			return (merger_list[length // 2 - 1] + merger_list[length // 2]) / 2


print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
