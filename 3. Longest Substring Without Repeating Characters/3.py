class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        left = 0
        size = 0

        for right, char in enumerate(s):
            if char in hash and hash[char] >= left:
                left = hash[char] + 1
            size = max(size, right - left + 1)
            hash[char] = right
        return size
            