public class Solution {
    public int Reverse(int x) {
        bool isNegative = x < 0;

        string str = x.ToString().Trim('-');
        char[] charArray = str.ToCharArray();
        Array.Reverse(charArray);
        string reversedStr = new string(charArray);

        if (isNegative)
            reversedStr = "-" + reversedStr;

    try {
            return int.Parse(reversedStr);
        } catch (OverflowException) {
            return 0;
        }
    }
}