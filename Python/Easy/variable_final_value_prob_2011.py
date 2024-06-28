from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # a = operations.count("X++")
        # b = operations.count("++X")
        # c = operations.count("--X")
        # d = operations.count("X--")
        # return a + b - c - d
        x: int = 0

        for ops in operations:
            if ops == "--X" or ops == "X--":
                x -= 1
            if ops == "X++" or ops == "++X":
                x += 1

        return x



if __name__ == "__main__":
    sol = Solution()

    print(sol.finalValueAfterOperations(["--X", "X++", "X++"]))
    print(sol.finalValueAfterOperations(["++X", "++X", "X++"]))
    print(sol.finalValueAfterOperations(["X++", "++X", "--X", "X--"]))
