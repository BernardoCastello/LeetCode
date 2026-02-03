class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_jump = 0
        end = len(nums) -1

        for i, jump in enumerate(nums):
            if i > max_jump:
                return False

            max_jump = max(max_jump, i + jump)

            if max_jump >= end:
                return True


        



S = Solution()
s = S.canJump([1,1,1,0])
print(s)
