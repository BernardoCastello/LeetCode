public class Solution {
    public int MySqrt(int x) {

        int count = 0;
        for (int i = 1; x-i>=0;i = i + 2)
        {
            count++;
            x = x - i;
        }

        return count;
    }
}