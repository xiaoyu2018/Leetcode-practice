#include<iostream>
using namespace std;

int climbStairs(int n)
{
    int x1 = 0;
    int x2 = 0;
    int r = 1;

    for (int i = 0; i < n; ++i)
    {
        x1 = x2;
        x2 = r;
        
        r = x1 + x2;
    }
    return r;
}

int main()
{
    cout << climbStairs(2);
}