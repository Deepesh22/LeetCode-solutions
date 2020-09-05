# A string S of lowercase English letters is given. 
# We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:

# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.


class Solution:
    def partitionLabels(self, S: str): #creating start end interval for each char and merging overlaps and counting length of final intervals
        d = {}
        for idx, e in enumerate(S):
            if d.get(e):
                d[e][1] = idx
            else:
                d[e] = [idx, idx]
        intervals = sorted(d.values(), key = lambda x: x[0])
        st = [intervals[0]]
        for s, e in intervals:
            if st[-1][1] < s:
                st.append([s,e])
            else:
                if st[-1][1] <= e:
                    st[-1][1] = e
        print(st)
        return list(map(lambda x: x[1] - x[0] + 1, st))