from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        steps = 0
        for num in nums:
            if num % 3 != 0:
                steps += 1
        return steps


if __name__ == "__main__":
    sol = Solution()

    print(sol.minimumOperations([1, 2, 3, 4]))
    print(sol.minimumOperations([3, 6, 9]))
