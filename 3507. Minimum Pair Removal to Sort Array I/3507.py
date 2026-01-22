class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:

        numberOperation = 0
        isDecreasing = True

        while isDecreasing:
            if len(nums) == 1:
                return numberOperation
            
            isDecreasing = False

            minSum = [0,float('inf')]

            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    isDecreasing = True

                sumAd = nums[i] + nums[i+1]

                if sumAd < minSum[1]:
                    minSum[0] = i
                    minSum[1] = sumAd
            
            if isDecreasing == True:
                del nums[minSum[0]+1]
                nums[minSum[0]] = minSum[1]
                numberOperation += 1
            print(nums)

        return numberOperation
    

S = Solution()
print(S.minimumPairRemoval([689,-360,234,673,663,-741,480,860,-707,209,246,792,930,696,-305]))


        
        