public class Solution {
    public int ArithmeticTriplets(int[] nums, int diff) {
        int count = 0;
        int i = 0;
        int j = 1;

        for (int k = 2; k < nums.Count(); k++)
        {
            while(j<k && nums[k] - nums[j] > diff)
            {
                j++;
            }
            while(i<j && nums[j] - nums[i] > diff)
            {
                i++;
            }
            if (nums[k] - nums[j] == diff && nums[j] - nums[i] == diff)
            {
                count++;
            }
        }
        return count;
        
    }
}