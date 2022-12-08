
public partial class Solution
{
    public class MyComparer : IComparer<int>
    {
        public int Compare(int x, int y)
        {
            return y-x;
        }
    }
    public int[] GetLeastNumbers(int[] arr, int k)
    {
        if(k==0)
            return new int[] { };
        PriorityQueue<int, int> pq = new PriorityQueue<int, int>(k,new MyComparer());

        for (int i = 0; i < k; i++)
        {
            pq.Enqueue(arr[i], arr[i]);
        }

        for (int i = k; i < arr.Length; i++)
        {
            if(arr[i]<pq.Peek())
            {
                pq.Dequeue();
                pq.Enqueue(arr[i],arr[i]);
            }
        }

        int[] res = new int[k];

        for (int i = 0; i < k; i++)
        {
            res[i] = pq.Dequeue();
        }

        return res;
    }
}