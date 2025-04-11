class Solution:
    def isSymmetric(self, n: int):
        str_n = str(n)
        if len(str_n) % 2 != 0:
            return -1

        a, b = str_n[: len(str_n) // 2], str_n[len(str_n) // 2 :]
        int_a, int_b = [int(num) for num in a], [int(num) for num in b]
        if sum(int_a) == sum(int_b):
            return n

        return -1

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = []

        for num in range(low, high + 1):
            if self.isSymmetric(num) != -1:
                ans.append(num)

        return len(ans)


print(Solution().countSymmetricIntegers(1200, 1230))
