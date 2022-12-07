public partial class Solution
{
    // 快速幂，是指数在求和，用2进制遍历求和可以指数接近n，即达到O(log)时间复杂度。
    // 理论上进制越高逼近越快，n进制可以一步得到结果。
    // 但是实际操作中不同进制时间复杂度量级没有改变，并且计算机中位运算更方便
    public double MyPow(double x, int n)
    {
        if(n==0)
            return 1;

        double res = 1;
        bool flag = (n > 0);
        long N = n;

        N = N > 0 ? N : -N;

        while (N >0)
        {
            if((N &1)==1)
                res *= x;
            N >>= 1;
            x = x * x;
        }

        return flag ? res : 1 / res;
    }

    
}