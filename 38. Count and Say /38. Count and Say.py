"""
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

"""
class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        res = ""
        while n >= i:
            res = deepfunc(res, i)
            i += 1
        return  res

def deepfunc(res, n):
    if not res:
        return "1"
    else:
        symbol = None
        cnt = 0
        s = res
        res = ""
        for digit in s:
            if not symbol:
                symbol = digit
                cnt += 1
                continue
            if digit == symbol:
                cnt += 1
            else:
                res += str(cnt) + symbol
                symbol = digit
                cnt = 1
        res += str(cnt) + symbol
        return res

if __name__ == "__main__":
    c = Solution()
    print(c.countAndSay(4))