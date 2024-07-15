class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i for i in s.split() if i != " "][::-1])



if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().reverseWords("a good   example"))