public class Solution {
    public int[] PlusOne(int[] digits) {

        digits[^1] = digits[^1] + 1;

        if (digits[^1] < 10)
        {
            return digits;
        }

        for (int i = (digits.Length -1); i>=0; i--)
        {
            if (digits[i] == 10)
            {
                digits[i] = 0;
                if (i != 0)
                {
                    digits[i-1] = digits[i-1] + 1;
                }
            }
            else
            {
                return digits;
            }
            if (i == 0 && digits[0] == 0)
            {

                List<int> lista = digits.ToList();
                lista.Insert(0, 1);

                digits = lista.ToArray(); 
                return digits;
            }
        }
        return digits;
        
    }
}