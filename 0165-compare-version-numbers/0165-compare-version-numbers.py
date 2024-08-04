class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split("."), version2.split(".")
        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            num1 = int(version1[i]) if i < len(version1) else 0
            num2 = int(version2[j]) if j < len(version2) else 0
            if num1 != num2:
                # return -1 if str(num1) + str(num2) > str(num2) + str(num1) else 1
                return -1 if num1 < num2 else 1
            i += 1
            j += 1
        return 0