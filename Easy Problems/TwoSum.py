'''
Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


class Solution:

    def twoSum(self, nums, target):
        res = []
        for i in (range(len(nums)-1)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    res.append(i)
                    res.append(j)
                    break

        return res


if __name__ == '__main__':
    sol = Solution()
    print('First Test Case: ', end=' ')
    print('Pass' if sol.twoSum([2, 4, 6, 7], 9) == list([0, 3]) else 'Fail')
    print('Second Test Case: ', end=' ')
    print('Pass' if sol.twoSum([3, 8, 6, 7], 9) == list([0, 2]) else 'Fail')
    print('Third Test Case: ', end=' ')
    print('Pass' if sol.twoSum([2, 7, 11, 15], 9) == list([0, 1]) else 'Fail')
    print('Fourth Test Case: ', end=' ')
    print('Pass' if sol.twoSum([3, 2, 4], 6) == list([1, 2]) else 'Fail')
    print('Fifth Test Case: ', end=' ')
    print('Pass' if sol.twoSum([3, 3], 6) == list([0, 1]) else 'Fail')

#Verify space and time complexity