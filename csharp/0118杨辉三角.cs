public partial class Solution
{
    public IList<IList<int>> Generate(int numRows)
    {
        IList<IList<int>> res = new List<IList<int>>(){
            new List<int>(){-1},
            new List<int>(){1},
            new List<int>(){1,1},
        };

        if(numRows>2)
        {
            for (int i = 3; i<=numRows;i++)
            {
                IList<int> crt = new List<int>() { 1 };

                for (int j = 1; j < i-1; j++)
                {
                    crt.Add(res[i-1][j-1]+res[i-1][j]);
                }
                crt.Add(1);
                res.Add(crt);
            }
        }

        return res.Take(new Range(1, numRows+1)).ToList();
    }
}