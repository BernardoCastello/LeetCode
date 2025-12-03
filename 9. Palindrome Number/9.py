class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal = str(x)
        print(pal)

        if len(pal) == 1:
            return True
        for i in range(len(pal)//2):
            if pal[i] != pal[-i-1]:
                return False
        return True

s = Solution()
r= s.isPalindrome(5210125)
print(r)