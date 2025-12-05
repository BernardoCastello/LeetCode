class Solution:
    def myAtoi(self, s: str) -> int:
        number = ''

        for i in s:
            if i == ' ' and number == '':
                continue
            elif i in ['+', '-'] and number == '':
                number += i
            elif i.isdigit():
                number += i
            else:
                break
        try:
            if 2**31 -1 < int(number):
                return 2**31 -1
            elif -2**31 > int(number): 
                return -2**31
            else:   
                return int(number)
        except:
            return 0

        


S = Solution()
print(S.myAtoi("2147483648"))  # Output: -42