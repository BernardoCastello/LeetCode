public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> aux = new Dictionary<int, int>();
        for (int idx = 0; idx < nums.Length; idx++)
        {
            int num = nums[idx];
            int complemento = target -num;

            if (aux.ContainsKey(num))
            {
                return new int[] { aux[num], idx};
            }
            aux[complemento] = idx;
        }
        throw new ArgumentException("None.");
        
    }
}