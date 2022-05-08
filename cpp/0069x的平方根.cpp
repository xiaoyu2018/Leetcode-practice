#include<iostream>

using namespace std;


// 二分
int mySqrt1(int x)
{
    int left = 0;
    int right = x;
    long mid;
    while (true)
    {
        mid = (left + right) >> 1;

        if(mid*mid==x)
            return mid;
        else if(mid*mid<x)
        {
            if((mid+1)*(mid+1)>x)
                return mid;
            else
                left = mid + 1;
        }

        else
            right = mid - 1;
    }
}

// 牛顿迭代
int mySqrt2(int x)
{
    if(x==0)
        return 0;
    double x1 = x;
    double x2 = x;
    while(true)
    {
        x2 = 0.5 * (x1 + x / x1);
        if(abs(x1-x2)<1e-1)
            return int(x2);
        x1 = x2;
    }
}

int main()
{
    int x = 2147395599;
    cout << mySqrt2(x);
}