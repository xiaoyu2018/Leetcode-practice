public partial class Solution
{
    public int HammingWeight(uint n)
    {
        uint temp = 0;
        int res = 0;
        for (int i = 0; i < 32; i++)
        {
            temp = (uint)(1 << i);
            if((temp&n)!=0)
            {
                res++;
            }
        }

        return res;
    }
}