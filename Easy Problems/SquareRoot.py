'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
'''

class Solution:
    def mySqrt(self, x):
        sqRt = None
        isEven = True if x % 2 == 0 else False
        temp = x // 2
        while isEven:
            if temp * temp == x:
                sqRt = temp
                isEven = False
            elif temp * temp > x:
                temp = temp // 2
            else:
                SqRt = temp if (temp + 1) ** 2 > x else temp + 1
                isEven = False
                sqRt = temp
        # isOdd = True if x % 2 != 0 else False
        # while isOdd:
        #     if temp * temp > x:
        #         prev = temp
        #         temp = temp // 2
        #     elif temp * temp < x:
        #
        #     pass
        return sqRt


sol = Solution()
print(sol.mySqrt(8))
print(sol.mySqrt(16))
print(sol.mySqrt(64))
print(sol.mySqrt(256))
print(sol.mySqrt(18))
print(sol.mySqrt(25))

