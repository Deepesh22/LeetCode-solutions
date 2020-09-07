# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

class Solution:
    # Runtime: 28 ms
    # Memory Usage: 14 MB
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        rd = {}
        if len(pattern) == len(str.split()):
            for s, p in zip(str.split(), pattern):
                if d.get(p) and rd.get(s):
                    if d[p] != s and rd[s] != p:
                        return False
                elif d.get(p) and rd.get(s) == None:
                    return False
                elif d.get(p) == None and rd.get(s):
                    return False
                else:
                    d[p] = s
                    rd[s] = p
            return True
        return False
    

print(Solution().wordPattern(pattern = "abba", str = "dog cat cat dog")) #true
print(Solution().wordPattern(pattern = "abba", str = "dog cat cat fish")) #false
print(Solution().wordPattern(pattern = "aaaa", str = "dog cat cat dog")) #false
print(Solution().wordPattern(pattern = "abba", str = "dog dog dog dog")) #false