public class Solution {
    public int LongestConsecutive(int[] nums) {
        HashSet<int> hash = new HashSet<int>(nums);
        int longest = 0;
        foreach (int n in hash){
            if (!hash.Contains(n-1)){
                int count = 1;
                while (hash.Contains(n+count)){
                    count++;
                }
                longest = Math.Max(longest, count);
            }
        }
        return longest;
    }
}