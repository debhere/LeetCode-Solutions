
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx: int = -1
        for i in range(len(nums)):
            if nums[i] == target:
                idx = i
                break
            if nums[i] > target and idx == -1:
                idx = i
            if i == len(nums) - 1 and idx == -1:
                idx = i + 1
        return idx


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))
    print(sol.searchInsert([1, 3, 5, 6], 2))
    print(sol.searchInsert([1, 3, 5, 6], 7))
