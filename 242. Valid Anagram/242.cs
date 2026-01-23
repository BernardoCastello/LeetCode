public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
        {
            return false;
        }

        int[] charCount = new int[256];
        for (int o = 0; i < s.Length; i++)
        {
            charCount[s[i]]++;
            charCount[t[i]]--;
        }
        foreach(int count in charCount)
        {
            if (count != 0)
            {
                return false;
            }
        }
        return true;
    }
}