class Solution:
    # def mySqrt(self, x: int) -> int:
    #     square_root: int = 1
    #     for num in range(1, x):
    #         if num * num == x:
    #             square_root = num
    #             break
    #         if num * num > x:
    #             square_root = num - 1
    #             break
    #     return square_root if x >= 1 else 0

    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        r: float = x // 2
        while r_ := (r + x / r) / 2:
            if int(r) == int(r_):
                return int(r)
            r = r_


if __name__ == "__main__":
    sol = Solution()

    print(sol.mySqrt(4))
    print(sol.mySqrt(8))
    print(sol.mySqrt(1))
    print(sol.mySqrt(0))
