class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        
        isZero = False
        negativeCount = 0
        absolute = 0
        minValue = 100000

        for i in matrix:
            for j in i:
                if j == 0:
                    isZero = True
                elif j < 0:
                    negativeCount += 1
                if abs(j) < minValue:
                    minValue = abs(j)
                absolute += abs(j)
        
        if negativeCount % 2 == 0 or isZero:
            return absolute
        else:
            print(minValue)
            return absolute - abs(2*minValue)




S = Solution()
print(S.maxMatrixSum([[10,-6,-6,-8],[-3,-7,-8,-9],[-4,-8,-5,-8],[-9,-9,-6,-8]]))
