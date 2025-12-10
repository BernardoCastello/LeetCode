class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        digits[-1] = digits[-1] + 1
        
        if digits[-1] < 10:
            return digits
        
        for i in range(len(digits)-1, -1,-1):
            
            if digits[i] == 10:
                digits[i] = 0
                if i != 0:
                    digits[i-1] +=1

            else:
                print("Aki")
                return digits
            
            if i == 0 and digits[i] == 0:
                digits.insert(0,1)

            
        return digits



S = Solution()
print(S.plusOne([1,8,9]))