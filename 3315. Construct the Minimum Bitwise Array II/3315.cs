public class Solution {
    public int[] MinBitwiseArray(IList<int> nums) {
        List<int> output = new List<int>();

        foreach (int i in nums)
        {
            if (i == 2)
            {
                output.Add(-1);
            }
            else
            {
                output.Add(i-((i+1) & -(i+1))/2);
            }
        }
        return output.ToArray();

    }
}