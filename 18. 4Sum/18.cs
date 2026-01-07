public class Solution {
    public IList<IList<int>> FourSum(int[] nums, int target) {
        Array.Sort(nums);
        int n = nums.Length; 
        IList<IList<int>> answer = new List<IList<int>>(); 

        for (int i = 0; i < n - 3; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            if ((long)nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target) 
                break;
            
            if ((long)nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target) 
                continue;

            for (int j = i + 1; j < n - 2; j++)
            {
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;

                if ((long)nums[i] + nums[j] + nums[j+1] + nums[j+2] > target) 
                    break;
                
                if ((long)nums[i] + nums[j] + nums[n-1] + nums[n-2] < target) 
                    continue;

                int k = j + 1;
                int l = n - 1;

                while (k < l)
                {
                    long currentSum = (long)nums[i] + nums[j] + nums[k] + nums[l];

                    if (currentSum == target)
                    {
                        answer.Add(new List<int> { nums[i], nums[j], nums[k], nums[l] });
                        
                        k++;
                        l--;

                        while (k < l && nums[k] == nums[k - 1]) k++;
                        while (k < l && nums[l] == nums[l + 1]) l--;
                    }
                    else if (currentSum < target)
                    {
                        k++;
                    }
                    else
                    {
                        l--;
                    }
                }
            }
        }
        return answer;
    }
}