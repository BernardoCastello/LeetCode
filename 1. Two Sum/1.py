class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        aux = {}
        for idx, num in enumerate(nums):
            if aux.get(num) is not None:
                return [aux.get(num), idx]
            aux[target-num] = idx