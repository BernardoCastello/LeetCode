public class Solution {
    public IList<IList<int>> MinimumAbsDifference(int[] arr) {
        Array.Sort(arr);

        List<IList<int>> answer = new List<IList<int>>();
        int minSum = int.MaxValue;

        for (int i = 0; i < arr.Length -1 ; i++)
        {
            int diff = arr[i+1] - arr[i];

            if (diff < minSum)
            {
                minSum = diff;
                answer.Clear();
                answer.Add(new List<int> { arr[i], arr[i+1] });
            } else if (diff == minSum)
            {
                answer.Add(new List<int> { arr[i], arr[i+1] });
            }
        }
        return answer;
        
    }
}