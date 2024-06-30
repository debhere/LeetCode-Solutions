from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        idx_list = [idx for idx, word in enumerate(words) if x in word]
        return idx_list


if __name__ == "__main__":
    sol = Solution()

    print(sol.findWordsContaining(["leet", "code"], 'e'))
    print(sol.findWordsContaining(["abc","bcd","aaaa","cbc"], 'a'))