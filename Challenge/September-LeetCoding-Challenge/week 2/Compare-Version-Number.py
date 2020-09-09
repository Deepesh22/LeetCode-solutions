# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        v1 = v1 + [0]*(len(v2)-len(v1)) if len(v1) < len(v2) else v1
        v2 = v2 + [0]*(len(v1)-len(v2)) if len(v1) > len(v2) else v2
        v1 = int(''.join(map(str, v1)))
        v2 = int(''.join(map(str, v2)))
        # print(v1, v2)
        if v1 == v2:
            return 0
        else:
            if v1 > v2:
                return 1
            else:
                return -1