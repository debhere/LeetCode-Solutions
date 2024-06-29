from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])
        return ans


if __name__ == "__main__":
    sol = Solution()

    print(sol.shuffle([2, 5, 1, 3, 4, 7], 3))
    print(sol.shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
