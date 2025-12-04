public class Solution {
    public bool IsPalindrome(int x) {
        string str = x.ToString();
        if (str.Length == 1)
            return true;
        char[] charArray = str.ToCharArray();
        for (int i = 0; i< charArray.Length / 2; i++) {
            if (charArray[i] != charArray[charArray.Length - 1 - i])
                return false;
        }
        return true;
    }
} // Not the most efficient solution but straightforward to understand