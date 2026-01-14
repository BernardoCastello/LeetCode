public class Solution {
    public void SortColors(int[] nums) {

        int low = 0;
        int mid = 0;
        int hig = nums.Length - 1;

        while(mid <= hig)
        {
            if (nums[mid] == 0)
            {
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;

                low++;
                mid++;

            }
            else if (nums[mid] == 1)
            {
                mid++;
            }
            else
            {
                int temp = nums[hig];
                nums[hig] = nums[mid];
                nums[mid] = temp;

                hig--;
            }

        }
        
    }
}