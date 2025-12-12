using System.ComponentModel.DataAnnotations;
using System.Globalization;

public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        List<IList<int>> output = new List<IList<int>>();

        for (int i = 0; i < nums.Length - 2; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1])
            {
                continue;
            }

            int j = i + 1;
            int k = nums.Length - 1;

            while (j < k)
            {
                int total = nums[i] + nums[j] + nums[k];

                if (total == 0)
                {
                    output.Add(new List<int> { nums[i], nums[j], nums[k] });

                    while (j < k && nums[j] == nums[j + 1]) {
                        j++;
                    }
                    
                    while (j < k && nums[k] == nums[k - 1]) {
                        k--;
                    }
                    
                    j++;
                    k--;
                } 
                else if (total < 0)
                {
                    j++;
                } 
                else
                {
                    k--;
                }
            }
        }
        return output;
    }
}