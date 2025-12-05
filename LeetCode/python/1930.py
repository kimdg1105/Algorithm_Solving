class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_dict = {}
        ans = 0

        for c in s:
            if c not in char_dict:
                char_dict[c] = 1
            else:
                char_dict[c] += 1
        print(char_dict)

        for char in char_dict:
            if char_dict[char] >= 2:
                if char_dict[char] >= 3:
                    # 자기도 포함
                    ans += len(char_dict)
                else:
                    # 자기빼고 전부 ++
                    ans += len(char_dict) - 1

        return ans


print(Solution().countPalindromicSubsequence("aabca"))
print(Solution().countPalindromicSubsequence("abc"))
print(Solution().countPalindromicSubsequence("bbcbaba"))
