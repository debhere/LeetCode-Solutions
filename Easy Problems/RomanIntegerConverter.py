class Solution(object):
    def romanToInt(self, x):
        roman_to_int_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        special = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 500, 'CM': 900}
        resultInt = 0
        allKeys = list(roman_to_int_mapping.keys()) + list(special.keys())
        print(allKeys)


if __name__ == '__main__':
    sol = Solution()
    sol.romanToInt('c')
