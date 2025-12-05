public class Solution {
    public int MyAtoi(string s) {
        string number = s.Trim(' ');
        int isPos = 1;
    
        double num = 0; 

        if (number == ""){
            return 0;
        }

        if (number[0] == '+' || number[0] == '-'){
            if (number[0] == '-'){
                isPos = -1;
            }
            number = number.Substring(1);
        }

        foreach (char c in number){
            if (!char.IsDigit(c)){
                break;
            }
            num = num * 10 + (c - '0');
        }

        num *= isPos;

        if (num < int.MinValue) return int.MinValue;
        if (num > int.MaxValue) return int.MaxValue;

        return (int)num;
    }
}