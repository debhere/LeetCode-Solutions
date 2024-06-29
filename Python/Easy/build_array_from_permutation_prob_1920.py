from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> list[int]:
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.buildArray([0, 2, 1, 5, 3, 4]))
    print(sol.buildArray([5, 0, 1, 2, 3, 4]))
