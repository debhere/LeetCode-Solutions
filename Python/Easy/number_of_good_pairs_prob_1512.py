from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Solution 1
        # count = 0
        # for i in range(0, len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        #
        # return count

        elements = defaultdict(int)
        count = 0

        for num in nums:
            count += elements[num]
            elements[num] += 1

        return count


if __name__ == "__main__":
    sol = Solution()

    print(sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(sol.numIdenticalPairs([1, 1, 1, 1]))
    print(sol.numIdenticalPairs([1, 2, 3]))
