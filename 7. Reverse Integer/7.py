class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        r = ""
        for i in range(len(x)):
            if x[i] == '-':
                r += '-'
                r += x[-i-1]
            else:
                if x[-i-1] != '-':
                    r += x[-i-1]
        r = int(r)
        if -2147483648<r<2147483647:
            return r
        else:
            return 0