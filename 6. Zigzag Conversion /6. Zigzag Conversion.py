"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return  s
        matrix = [["" for _ in range(len(s))] for _ in range(numRows)]
        col = 0
        row = 0
        for i, v in enumerate(s):
            if col % (numRows - 1) == 0:
                matrix[row][col] = v
                row += 1
                if row == numRows:
                    col = col + 1
                    row -= 2
            else:
                matrix[row][col] = v
                col += 1
                row -= 1
        matrix = ''.join(["".join(i) for i in matrix])
        return matrix
        

if __name__ == "__main__":
    s, numRows = input().split(" ")
    numRows = int(numRows)
    c = Solution()
    print(c.convert(s, numRows))

