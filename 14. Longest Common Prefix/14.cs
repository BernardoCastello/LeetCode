public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        string pre = strs[0];
        for (int i = 1; i < strs.Length; i++) 
        {
            while (!strs[i].StartsWith(pre) && pre.Length > 0)
            {

                pre = pre.Substring(0, pre.Length - 1);
                
                if (pre.Length == 0) 
                {
                    return "";
                }
            }
        }
        return pre;
    }
}