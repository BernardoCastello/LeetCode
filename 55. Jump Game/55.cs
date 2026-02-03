using System.Diagnostics;

public class Solution {
    public bool CanJump(int[] nums) {
        int max_jump = 0;
        int end = nums.Count() - 1;

        for (int i = 0; i <= end; i++)
        {
            if (i > max_jump)
            {
                return false;
            }
            max_jump = Math.Max(max_jump, i+nums[i]);

            if (max_jump >= end)
            {
                return true;
            }
        }

        return true;
        
    }
}