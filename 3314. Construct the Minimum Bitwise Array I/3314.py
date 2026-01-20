class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        output = []

        for i in nums:
            if i == 2:
                output.append(-1)

            else:
                low = (i+1) & -(i+1)
                output.append(i - (low //2))

        return output
    
S = Solution()
print(S.minBitwiseArray([11,13,31]))

