from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: [TreeNode]) -> int:

        queue = deque([root])


        big_level = 0
        big_sum = -100000

        lvl = 0
        while queue:

            sum_lvl = 0

            for _ in range(len(queue)):
                node = queue.popleft()

                sum_lvl += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if sum_lvl > big_sum:
                big_sum = sum_lvl
                big_level = lvl

            lvl += 1
        return big_level


