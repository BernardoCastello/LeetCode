class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        valid = False
        answer = 0
        while True:

            if s[-1] != " ":
                if valid == False:
                    valid = True
                answer += 1
                s = s[:-1]

                if len(s) == 0:
                    return answer
            

            elif s[-1] == " ":
                if valid == True:
                    return answer
                s = s[:-1]
            
            
            if len(s) == 0:
                return answer


S = Solution()
print(S.lengthOfLastWord("Hello World"))