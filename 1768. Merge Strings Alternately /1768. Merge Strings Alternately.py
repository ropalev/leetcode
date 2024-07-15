class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = list(zip(word1, word2))

        if len(word2) > len(word1):
            return "".join(map(lambda x: "".join(x), s))+word2[len(s):]
        elif len(word1) > len(word2):
            return "".join(map(lambda x: "".join(x), s))+word1[len(s):]
        return "".join(map(lambda x: "".join(x), s))




if __name__ == "__main__":
    print(Solution().mergeAlternately("abc", "prq"))
    print(Solution().mergeAlternately("ab", "pqrs"))
    print(Solution().mergeAlternately("abcd", "pq"))
