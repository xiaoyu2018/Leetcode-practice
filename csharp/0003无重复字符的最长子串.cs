public partial class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        Queue<char> que = new();
        int res = 1;
        if(s.Length>0)
        {
            que.Enqueue(s[0]);

            foreach (char item in s[1..])
            {
                while (que.Contains(item))
                {
                    que.Dequeue();
                }

                que.Enqueue(item);
                res = Math.Max(res, que.Count);
            }
        }

        else
            return 0;

        return res;
    }
}