public class Solution {
    public int LengthOfLastWord(string s) {
        int lenght = 0;
        int i = s.Count() - 1;

        while(i >=0 && s[i] == ' ')
        {
            i--;
        }
        while(i>=0 && s[i] != ' ')
        {
            lenght++;
            i--;
        }
        return lenght;
    }
}