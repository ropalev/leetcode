class Solution:
    roman_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    def romanToInt(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            if s[i] in ("I","X","C"):
                try:
                    result += self.roman_dict[s[i:i+2]]
                    i += 1
                except:
                    result += self.roman_dict[s[i]]
            else:
                result +=  self.roman_dict[s[i]]
            i += 1
        return result


if __name__ == '__main__':
    c = Solution()
    print(c.romanToInt("III"))
    print(c.romanToInt("LVIII"))
    print(c.romanToInt("MCMXCIV"))
    print(c.romanToInt("IX"))
