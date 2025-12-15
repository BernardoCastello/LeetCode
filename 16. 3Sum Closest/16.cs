using System.Data.Common;

public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        Array.Sort(nums);
        int closestSum = nums[0] + nums[1] + nums[2];

        if (nums.Length == 3)
        {
            return closestSum;
        }

        for(int i = 0; i < nums.Length -2; i++)
        {
            if (i>0 && nums[i] == nums[i - 1])
            {
                continue;
            }

            int j = i + 1;
            int k = nums.Length - 1;

            while (j < k)
            {

                int sumNums = nums[i] + nums[j] + nums[k];

                if (sumNums == target)
                    {
                        return sumNums;
                    }
                
                if (Math.Abs(target - sumNums) < Math.Abs(target - closestSum))
                {
                    closestSum = sumNums;
                }

                if (sumNums > target)
                {
                    k--;
                } else if (sumNums < target)
                {
                    j++;
                }
            }
        }
        return closestSum;
    }
}