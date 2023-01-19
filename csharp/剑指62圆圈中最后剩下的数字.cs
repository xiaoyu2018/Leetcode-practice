public partial class Solution
{
    public int LastRemaining(int n, int m)
    {
        int res = 0;

        for (int i=2;i<=n ;i++ )
        {
            res = (m + res) % i;
        }
        return res;
    }
}