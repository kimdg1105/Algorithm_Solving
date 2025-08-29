from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> str:
        arr = []
        result = ""
        for idx, char in enumerate(s):
            l, r = idx - 1, idx + 1
            while l >= 0 and r < len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            arr.append(s[l : r + 1])
        print(arr)
        return result


print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("babad"))
