import itertools
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        hash = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        digits_numbers = []

        for i in digits:
            digits_numbers.append(list(hash[i]))

        combinations = list(map(''.join, itertools.product(*digits_numbers)))


        return combinations

S = Solution()
print(S.letterCombinations("234"))
print(S.letterCombinations("2"))
