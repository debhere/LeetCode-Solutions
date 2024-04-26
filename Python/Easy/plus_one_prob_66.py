from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ''
        for digit in digits:
            nums += str(digit)
        nums = int(nums)
        nums += 1
        digits = [int(num) for num in str(nums)]
        return digits

if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))
    print(sol.plusOne([4, 3, 2, 1]))
    print(sol.plusOne([9]))
    print("My testcase")
    print(sol.plusOne([4, 3, 2, 9]))
