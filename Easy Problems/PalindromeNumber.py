'''

Given an integer x, return true if x is a
palindrome, and false otherwise.

WITHOUT CONVERTING TO STRING
'''


class Solution(object):
    def isPalindrome(self, x):
        numIsPalindrome = False
        y = 0
        rem = 0
        digitList = []
        temp = x
        while temp > 9:
            digitList.append(temp % 10)
            temp = temp // 10
            rem = temp % 10

        digitList.append(rem)
        mul = 1
        for i in range(1, len(digitList)):
            mul *= 10

        for digit in digitList:
            y = y + (digit * mul)
            mul //= 10

        if (x == y) or (x in range(0, 10)):
            numIsPalindrome = True

        return numIsPalindrome


if __name__ == '__main__':
    sol = Solution()
    # sol.isPalindrome(121)
    print('First Test Case: ', end=' ')
    print('Pass' if sol.isPalindrome(121) else 'Fail')
    print('Second Test Case: ', end=' ')
    print('Pass' if not sol.isPalindrome(-121) else 'Fail')
    print('Third Test Case: ', end=' ')
    print('Pass' if not sol.isPalindrome(10) else 'Fail')
    print('Fourth Test Case: ', end=' ')
    print('Pass' if sol.isPalindrome(222) else 'Fail')
    print('Fifth Test Case: ', end=' ')
    print('Pass' if not sol.isPalindrome(5252) else 'Fail')
    print('Sixth Test Case: ', end=' ')
    print('Pass' if sol.isPalindrome(1) else 'Fail')
    print('Seventh Test Case: ', end=' ')
    print('Pass' if sol.isPalindrome(505) else 'Fail')
