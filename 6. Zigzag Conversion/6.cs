using System.Diagnostics;

public class Solution {
    public string Convert(string s, int numRows) {
        bool growing = true;
        int counter = 0;
        string zigzag = "";
        string[] rows = new string[numRows];

        if (numRows == 1)
        {
            return s;
        }

        foreach (char c in s)
        {
            if (growing)
            {
                rows[counter] = rows[counter] + c;

                if (counter == numRows - 1)
                {
                    growing = false;
                    counter--;
                    continue;
                }
                counter++;
            }
            else
            {
                rows[counter] = rows[counter] + c;

                if (counter == 0)
                {
                    growing = true;
                    counter++;
                    continue;
                }
                counter--;
            }
        }

        foreach (string str in rows)
        {
            zigzag = zigzag + str;
        }

        return zigzag;
    }
}