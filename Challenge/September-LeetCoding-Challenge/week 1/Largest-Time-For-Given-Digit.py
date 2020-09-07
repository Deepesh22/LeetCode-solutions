from itertools import permutations


# Given an array of 4 digits, return the largest 24 hour time that can be made.

# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.


class Solution:
    def largestTimeFromDigits(self, A):
        ans = ''
        for perm in permutations(A):
            if ((perm[0] == 2 and perm[1] < 4) or (perm[0] < 2)) and perm[2] < 6:
                temp = ''.join(map(str, perm[:2])) + ':' + ''.join(map(str, perm[2:]))
                if ans < temp:
                    ans = temp
        return ans


print(Solution().largestTimeFromDigits([1,2,3,4])) # "23:41"