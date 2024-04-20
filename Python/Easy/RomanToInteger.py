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
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX').replace('XC', 'LXXXX').replace('CD',
                                                                                                                'CCCC').replace(
            'CM', 'DCCCC')
        return sum(map(lambda x: roman_to_int_mapping[x], s))


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
    print('Fifth Test Case: ', end='')
    print('Pass' if sol.romanToInt('LVIII') == 58 else 'Fail')
    print('Sixth Test Case: ', end='')
    print('Pass' if sol.romanToInt('III') == 3 else 'Fail')
    print('Seventh Test Case: ', end='')
    print('Pass' if sol.romanToInt('MCMXCIV') == 1994 else 'Fail')
