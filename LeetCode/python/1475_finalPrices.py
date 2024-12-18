from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i, value in enumerate(prices):
            sale = 0
            if i != len(prices) - 1:
                for j in range(i + 1, len(prices)):
                    if prices[j] <= value:
                        sale = prices[j]
                    if sale != 0:
                        break

            ans.append(value - sale)

        return ans


sol = Solution()
print(sol.finalPrices([1, 2, 3, 4, 5]))
print(sol.finalPrices([8, 4, 6, 2, 3]))
