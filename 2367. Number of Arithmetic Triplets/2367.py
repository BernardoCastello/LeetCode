class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        output = 0

        for i in range (len(nums)-2):

            j = i + 1
            k = len(nums) -1

            if nums[j] - nums[i] > diff:
                continue
            
            while j < k:
                if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                    output += 1
                    j += 1
                    k -= 1
                    continue

                if nums[j] - nums[i] < diff:
                    j += 1
                    continue

                k -= 1

        return output


S = Solution()
print(S.arithmeticTriplets([0,1,4,6,7,10],3))            


