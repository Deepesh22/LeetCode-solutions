# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
# You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

from collections import Counter

class Solution:
    # memory less than 90% of submissions
    def slowRepeatedSubstringPattern(self, s: str) -> bool:
        ls = len(s)
        if ls == 0:
            return True
        else:
            ss = ''
            for i in s[: ls//2 + 1]:
                ss += i
                c = s.count(ss)
                if len(ss)*c == ls and c != 1:
                    # print(ss)
                    return True
            return False

    # runtime beats 94% of submissions
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = len(s)
        if ls < 2:
            return False
        else:
            if len(set(s)) == 1:
                return True
            else:
                for i in [2, 3, 5, 7]:
                    if ls % i == 0:
                        if s[:ls//i] * i == s:
                            return True
                return False

print(Solution().repeatedSubstringPattern('abab')) #True
print(Solution().repeatedSubstringPattern('ababab')) #True
print(Solution().repeatedSubstringPattern('abababa')) #False