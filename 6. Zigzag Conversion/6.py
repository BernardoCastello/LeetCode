class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [""]*numRows
        growing = True
        counter = 0
        zigzag = ""

        if numRows == 1:
            return s

        for i in s:
            rows[counter] += i
            if growing:

                if counter == numRows -1:
                    growing = False
                    counter -= 1
                    continue

                counter += 1

            else:
                if counter == 0:
                    growing = True
                    counter += 1
                    continue
                
                counter -= 1

        for i in rows:
            zigzag += i
        
        return zigzag
    

print(Solution().convert("ABC", 1))