class Solution:
    def reverseVowels(self, s: str) -> str:
        j = len(s) - 1
        i = 0
        l = list(s)
        while i < j:
            if i < j and l[i] in "aoueiAOUEI":
                while i < j:
                    if l[j] in "aoueiAOUEI":
                        l[i], l[j] = l[j], l[i]
                        j -= 1
                        break
                    j -= 1
            i += 1
        return "".join(l)


if __name__ == "__main__":
    print(Solution().reverseVowels("u'o;B,vKO\"?,.;?fGI 9;`9T`Z,;iqsn4A.:;'H3s8E9. B4TxfOiB'wvM?q'k:Q`J\"E1T7lo e7c!?glI66?JZh\"6 !C,aK! 1J?f9'`SX4Q!Q4XS`'9f?J1 !Ka,C! 6\"hZJ?66Ilg?!c7e ol7T1E\"J`Q:k'q?Mvw'BiOfxT4B .9E8s3H';:.A4nsqi;,Z`To`;o IGf?;.,?\"OKv,B;o'u"))
    print(Solution().reverseVowels("hellO"))
    print(Solution().reverseVowels("leetcode"))
    print(Solution().reverseVowels("asdofnvawoirutyra"))
