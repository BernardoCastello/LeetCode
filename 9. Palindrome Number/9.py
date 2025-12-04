class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal = str(x)

        if len(pal) == 1:
            return True
        for i in range(len(pal)//2):
            if pal[i] != pal[-i-1]:
                return False
        return True