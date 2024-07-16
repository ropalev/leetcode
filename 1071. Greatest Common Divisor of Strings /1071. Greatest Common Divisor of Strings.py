class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        l = len(str2)
        while l:
            if len(str1) % l or len(str2) % l:
                l -= 1
                continue
            if ((str2[:l] * (len(str1) // l)) == str1) and ((str2[:l] * (len(str2) // l)) == str2):
                return str2[:l]
            l -= 1
        return ""


if __name__ == "__main__":
    print(Solution().gcdOfStrings("ABCABC", "ABC"))
    print(Solution().gcdOfStrings("ABABAB", "ABAB"))
    print(Solution().gcdOfStrings("LEET", "CODE"))
    print(Solution().gcdOfStrings("AAAAAAAAA", "AAACCC"))
