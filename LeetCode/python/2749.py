class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        val = num1
        for i in range(61):
            val = num1 - (pow(2, i) + num2)
            print(val)

        return 0


print(Solution().makeTheIntegerZero(3, -2))
