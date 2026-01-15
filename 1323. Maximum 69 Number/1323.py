class Solution:
    def maximum69Number (self, num: int) -> int:
        
        div = 10000
        answer = 0
        change = False

        while div >= 1:

                if num // div == 0:
                    div = div / 10
                    continue

                if num // div == 9:
                    answer = (answer * 10) + (num // div)
                    num = num % div
                    div = div / 10
                    continue

                else:
                    if change == False:
                        num = num % div
                        div = div / 10
                        answer = (answer * 10) + 9
                        change = True
                    else:
                        num = num % div
                        div = div / 10
                        answer = (answer * 10) + 6
                         


        return int(answer)
    
S = Solution()
print(S.maximum69Number(6969969))
