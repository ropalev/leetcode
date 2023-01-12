def same_kind(open_b, close_b: str) -> bool:
    if close_b == ")" and open_b == "(":
        return True
    elif close_b == "}" and open_b == "{":
        return True
    elif close_b == "]" and open_b == "[":
        return True
    return False

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list(s)
        stack = []
        if (s[0] not in ["(", "[", "{"]) or (len(s) % 2 != 0):
            return False
        for bracket in s:
            if bracket in ["(", "[", "{"]:
                brackets.pop(0)
                stack.append(bracket)
            else:
                if stack and same_kind(stack[-1], bracket):
                    stack.pop()
                    brackets.pop(0)
                else: break
        if not stack and not brackets:
            return True
        return False


if __name__ == '__main__':
    c = Solution()
    print(c.isValid("]"))
    print(c.isValid("[{(})]"))
    print(c.isValid("[[]{}[()]]"))
    print(c.isValid("(){}}{"))
        
