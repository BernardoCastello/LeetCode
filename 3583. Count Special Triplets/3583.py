from collections import Counter

class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        left = Counter()
        right = Counter(nums)

        count = 0

        for x in nums:
            print(x, left, right)
            right[x] -= 1
            if right[x] == 0:
                del right[x]

            target = x * 2
            if target in left and target in right:
                count += left[target] * right[target]

            left[x] += 1

        MOD = 10**9 + 7
        return count % MOD

    
S=Solution()

print(S.specialTriplets([84,2,93,1,2,2,26]))