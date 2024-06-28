from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Solution 1
        ans = nums[:] # can be done with ans = nums.copy() but more execution time
        ans = ans + nums
        return ans

        #Solution 2
        # return nums * 2

        #Solution 3
        #return [*nums, *nums]



if __name__ == "__main__":
    sol = Solution()

    print(sol.getConcatenation([1, 2, 1]))
    print(sol.getConcatenation([1, 3, 2, 1]))