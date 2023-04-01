"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""


from typing import  List
from itertools import combinations_with_replacement, combinations, product

DIGITS_MAP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, n: str) -> List[str]:
        # Return an empty list if n is an empty string
        if n == '':
            return []

        # List of options for each digit on the keypad
        options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        # Initialize queue with an empty string
        queue = [""]

        # Loop over each digit in n
        for digit in n:
            # Convert digit to integer
            digit = int(digit)
            # Loop over the length of queue
            for _ in range(len(queue)):
                # Remove the first element in queue and store it in curr
                curr = queue.pop(0)
                # Append the concatenation of curr and each character in the set of characters corresponding to digit in options to queue
                for letter in options[digit]:
                    queue.append(curr + letter)

        # Return the list of combinations stored in queue
        return queue

if __name__ == "__main__":
    digits = input()
    c = Solution()
    print(c.letterCombinations(digits))


