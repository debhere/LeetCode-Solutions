class Solution:
    def lengthOflastWord(self, s: str) -> int:
        s = s.strip()
        words = s.split(' ')
        return len(words[-1])


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOflastWord("Hello World"))
    print(sol.lengthOflastWord("   fly me   to   the moon  "))
    print(sol.lengthOflastWord("luffy is still joyboy"))
