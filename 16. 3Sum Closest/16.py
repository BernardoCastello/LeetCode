class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]

        if len(nums) == 3:
            return closestSum


        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) -1

            while j<k:
                sumNums = nums[i] + nums[j] + nums[k]

                if abs(target - sumNums) < abs(target - closestSum):
                    closestSum = sumNums
                if closestSum == target:
                    return closestSum
                
                if sumNums > target:
                    k -= 1

                elif sumNums < target:
                    j += 1
            
        return closestSum
        

S = Solution()
print(S.threeSumClosest([1,1,1,1], 3))

                
