"""
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
"""


"""
1-9 9
10 - 99 90
100 -999 900

12345
start size step 1,1,9
n size,step,start = 12336,2,90,10
12336
start size step 2,90,10
12246
n size,step,start = 12246,3,900,100
9546
1000 + 9545 // 3 = 3515

"""
class Solution:
    def findNthDigit(self, n):
        start, lenght, next = 1,1,9
        while n > lenght * next:
            n = n - lenght * next
            lenght +=1
            next *= 10
            start *= 10
        else:
            return int(str(start +(n-1) // lenght)[(n-1) % lenght])

if __name__ == "__main__":
    n = 11
    c = Solution()
    print(c.findNthDigit(n))


