class Solution:
    def mySqrt(self, x: int) -> int:
        count = 0
        i = 1
        while x-i>=0:
            count += 1
            x -= i
            i += 2

        return count