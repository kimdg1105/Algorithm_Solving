from typing import List


class Solution:
	def minOperations(self, grid: List[List[int]], x: int) -> int:
		num_list = [num for row in grid for num in row]

		num_list.sort()
		mid = len(num_list) // 2
		cnt = 0
		for n in num_list:
			if abs(n - num_list[mid]) % x != 0:
				return -1
			else:
				cnt += abs(n - num_list[mid]) // x
		return cnt


print(Solution().minOperations([[1, 5], [2, 3]], 1))
