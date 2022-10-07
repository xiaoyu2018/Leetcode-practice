public partial class Solution
{
    public int BeautifulBouquet(int[] flowers, int cnt)
    {
        int size = flowers.Length;
        int[] dp = new int[100000];
        int[] temp = new int[100000];
        for (int i = 0; i < 100000; i++)
        {
            dp[i] = 1;
        }

        for (int i = 1; i < size; i++)
        {
            dp[i] = dp[i - 1];
            for (int x = 0; x < 100000; x++)
            {
                temp[x] = 0;
            }

            for (int j = i; j > -1; j--)
            {
                temp[flowers[j]] += 1;
                if (temp[flowers[j]] <= cnt)
                    dp[i] += 1;
                else
                    break;
            }
        }


        return dp[size - 1] % 1000000007;
    }
}