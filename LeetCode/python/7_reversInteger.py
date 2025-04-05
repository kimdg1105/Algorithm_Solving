class Solution:
    def reverse(self, x: int) -> int:
        is_negative = 1
        if x < 0:
            is_negative = -1

        str_int = str(abs(x))
        reversed = str_int [::-1]
        ans = int(reversed) * is_negative

        if -(2**31) > ans  or ans > 2**31:
            return 0
        return ans
    

    

print(Solution().reverse(1534236469))