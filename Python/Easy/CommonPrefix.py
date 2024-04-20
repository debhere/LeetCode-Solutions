'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        ref = min(strs, key=len)

        commonPrefix = ''
        for idx in range(1, len(ref)+1):
            if sum(map(lambda x: x.startswith(ref[:idx]), strs)) == len(strs):
                commonPrefix = ref[:idx]

        return commonPrefix


if __name__ == '__main__':
    sol = Solution()

    print('First Test Case: ', end='')
    print('Pass' if sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl" else 'Fail')
    print('Second Test Case: ', end='')
    print('Pass' if sol.longestCommonPrefix(["dog", "racecar", "car"]) == "" else 'Fail')
    print('Third Test Case: ', end='')
    print('Pass' if sol.longestCommonPrefix(["eye", "elephant", "energy"]) == "e" else 'Fail')
    print('Fourth Test Case: ', end='')
    print('Pass' if sol.longestCommonPrefix(["apple"]) == "apple" else 'Fail')
    print('Fifth Test Case: ', end='')
    print('Pass' if sol.longestCommonPrefix(["football", "football"]) == "football" else 'Fail')
