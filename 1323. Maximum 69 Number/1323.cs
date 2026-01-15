using System.Diagnostics;

public class Solution {
    public int Maximum69Number (int num) {

        int div = 10000;
        int answer = 0;
        bool change = false;

        while (div >= 1)
        {
            if (num / div == 0)
            {
                div = div / 10;
                continue;
            }
            if (num / div == 9)
            {
                answer = (answer * 10) + (num / div);
                num = num % div;
                div = div /10;
                continue;
            }
            else
            {
                if (change == false)
                {
                    num = num % div;
                    div = div / 10;
                    answer = (answer * 10) + 9;
                    change = true;
                }
                else
                {
                    num = num % div;
                    div = div / 10;
                    answer = (answer * 10) + 6;
                }
            }
        }
        return answer;
        
    }
}