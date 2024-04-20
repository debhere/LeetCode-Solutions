'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
'''

class Solution:
    def mySqrt(self, x):
        sqRT = None
        isEven = True if x % 2 == 0 else False
        temp = x // 2
        while isEven:
            if temp * temp == x:
                sqRT = temp
                isEven = False
            elif temp * temp > x:
                temp = temp // 2
            else:
                for i in range(1, 5):
                    if ((temp + i) ** 2) > x:
                        sqRT = temp #if (temp + 1) ** 2 > x else temp + 1
                        break
                    else:
                        temp = temp + i
                isEven = False
        return sqRT


sol = Solution()
print(sol.mySqrt(8))
print(sol.mySqrt(16))
print(sol.mySqrt(64))
print(sol.mySqrt(256))
print(sol.mySqrt(18))
print(sol.mySqrt(20))

