class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        low = 0
        mid = 0
        hight = len(nums) -1

        while mid<=hight:

            if nums[mid] == 0:

                aux = nums[low]
                nums[low] = nums[mid]
                nums[mid] = aux

                low+=1
                mid+=1
            
            elif nums[mid] == 1:
                mid+=1

            else:
                aux = nums[hight]
                nums[hight] = nums[mid]
                nums[mid] = aux

                hight -=1

            print(nums)

S = Solution()
print(S.sortColors([2,0,1]))



