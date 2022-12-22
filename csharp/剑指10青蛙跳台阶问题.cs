
public partial class Solution
{
    Dictionary<int, int> memo = new() { { 0, 1 }, { 1, 1 } };
    public int NumWays(int n)
    {
        if(n<2)
            return 1;
        int n1, n2;

        n1 = memo.Keys.Contains(n - 1) ? memo[n - 1] : NumWays(n - 1);
        n2 = memo.Keys.Contains(n - 2) ? memo[n - 2] : NumWays(n - 2);

        memo[n]=(int)((n1 + n2) % (1e9 + 7));
        return memo[n];
    }
}