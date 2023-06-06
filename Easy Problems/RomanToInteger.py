'''
Given Roman numerals, code should return the corresponding integers
eg: XV = 15
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_to_int_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        resultInteger = 0
        start = s[0]
        limit = len(s)
        for idx in range(1, limit):
            end = s[idx]
            if ((start == 'I' and end == 'V') or (start == 'I' and end == 'X') or
                    (start == 'X' and end == 'L') or (start == 'X' and end == 'C') or
                    (start == 'C' and end == 'D') or (start == 'C' and end == 'M')):
                resultInteger = resultInteger + (roman_to_int_mapping[end] - roman_to_int_mapping[start])
                start = end
            else:
                if (limit - idx) == 1:
                    resultInteger = resultInteger + (roman_to_int_mapping[end] + roman_to_int_mapping[start])
                else:
                    resultInteger = resultInteger + roman_to_int_mapping[start]
                    start = end

        return resultInteger


if __name__ == '__main__':
    sol = Solution()
    print('First Test Case: ', end='')
    print('Pass' if sol.romanToInt('XV') == 15 else 'Fail')
    print('Second Test Case: ', end='')
    print('Pass' if sol.romanToInt('IV') == 4 else 'Fail')
    print('Third Test Case: ', end='')
    print('Pass' if sol.romanToInt('IX') == 9 else 'Fail')
    print('Fourth Test Case: ', end='')
    print('Pass' if sol.romanToInt('XIX') == 19 else 'Fail')
    # print('Fifth Test Case: ', end='')
    # print('Pass' if sol.romanToInt('LVIII') == 58 else 'Fail')
    # print('Sixth Test Case: ', end='')
    # print('Pass' if sol.romanToInt('III') == 3 else 'Fail')
    # print('Seventh Test Case: ', end='')
    # print('Pass' if sol.romanToInt('MCMXCIV') == 1994 else 'Fail')
