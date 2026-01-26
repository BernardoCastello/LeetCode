class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        answer = []
        min_sum = float('inf')

        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]

            if diff < min_sum:
                min_sum = diff
                answer = [[arr[i], arr[i+1]]]

            elif diff == min_sum:
                answer.append([arr[i], arr[i+1]])


        return answer



S = Solution()
print(S.minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
