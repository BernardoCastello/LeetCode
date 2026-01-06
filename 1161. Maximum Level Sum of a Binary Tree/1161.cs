using System;
using System.Collections.Generic;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {
    private List<int> levelSums = new List<int>();

    public int MaxLevelSum(TreeNode root) {
        Dfs(root, 0);

        int maxLevel = 1; 
        int maxSum = int.MinValue;

        for (int i = 0; i < levelSums.Count; i++) {
            if (levelSums[i] > maxSum) {
                maxSum = levelSums[i];
                maxLevel = i + 1;
            }
        }

        return maxLevel;
    }

    private void Dfs(TreeNode node, int level) {
        if (node == null) return;

        if (level == levelSums.Count) {
            levelSums.Add(node.val);
        } 
        else {
            levelSums[level] += node.val;
        }

        Dfs(node.left, level + 1);
        Dfs(node.right, level + 1);
    }
}