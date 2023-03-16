package algorithm;

public class LC0050POW {
    private double _calc(double x, long n)
    {
        if(n==0)
            return 1;
        double res = _calc(x, n / 2);
        res *= res;
        if (n % 2 == 1)
            res *= x;
        return res;
    }

    public double myPow(double x, int n) 
    {
        boolean flag = n > 0;
        long N = n;
        double res = flag?_calc(x, N): _calc(x, -N);
        
        return flag ? res : 1 / res;
    }

}
