class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hash = set(nums)
        long = 0

        for i in hash:
            if (i-1) not in hash:
                aux = 1
                while (i+aux) in hash:
                    aux += 1
                long = max(long, aux)
        return long


S = Solution()
print(S.longestConsecutive([1,7,10]))
