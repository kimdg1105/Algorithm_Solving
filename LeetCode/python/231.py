class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        low, high = 0, 31
        checked = set()

        while low <= high:
            mid = (low + high) // 2
            if mid in checked:
                return False
            checked.add(mid)
            expected = 2**mid
            if expected == n:
                return True
            elif expected < n:
                low = mid
            else:
                high = mid

        return False


print(Solution().isPowerOfTwo(1))
print(Solution().isPowerOfTwo(16))
print(Solution().isPowerOfTwo(3))
