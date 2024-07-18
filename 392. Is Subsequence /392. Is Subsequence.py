class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(s):
            c = s[ptr1]
            while ptr2 < len(t):
                if c == t[ptr2]:
                    ptr2 += 1
                    break
                ptr2 += 1
            else:
                return False
            ptr1 += 1
        return True



if __name__ == "__main__":
    print(Solution().isSubsequence(s = "abc", t = "ahbgdc"))
    print(Solution().isSubsequence(s = "axc", t = "ahbgdc"))
    print(Solution().isSubsequence(s = "abc", t = "ahbgdc"))