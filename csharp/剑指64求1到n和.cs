public partial class Solution
{
    public int SumNums(int n)
    {
        // 利用逻辑运算的短路性质结束递归
        var temp=n>0 && (n+=SumNums(n - 1)) is int;
        return n;
    }
}