class Solution:

    def sortVowels(self, s: str) -> str:
        v = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        ans = ""
        base = list(s)
        vowels = []
        for idx, val in enumerate(base):
            if val in v:
                vowels.append(val)

        vowels.sort()

        for idx, val in enumerate(base):
            if val not in v:
                ans += val
            else:
                vowel = vowels.pop(0)
                ans += vowel

        return ans


print(Solution().sortVowels("lEetcOde"))
print(Solution().sortVowels("lYmpH"))
