from collections import defaultdict


class Solution:
	def longestPalindrome(self, s: str) -> str:
		char_list = []
		result = ""
		for idx, char in enumerate(s):
			char_list.append((idx,char))
		
		for idx, char in char_list:
			cur_result = char
			l,r = idx-1, idx+1

			while l >= 0 and r <= len(s):				
				if l > 0 and r < len(s):
					if s[l] == s[r]:
						cur_result = s[l] + s[idx] + s[r]
				
				if len(cur_result) >= len(result):
					result = cur_result
				l-=1
				r+=1


		return result


print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("babad"))

