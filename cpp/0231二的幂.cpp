#include<iostream>
#include<unordered_set>
#include<math.h>
using namespace std;

bool isPowerOfTwo1(int n)
{
    unordered_set<int> s = {1,
                            2,
                            4,
                            8,
                            16,
                            32,
                            64,
                            128,
                            256,
                            512,
                            1024,
                            2048,
                            4096,
                            8192,
                            16384,
                            32768,
                            65536,
                            131072,
                            262144,
                            524288,
                            1048576,
                            2097152,
                            4194304,
                            8388608,
                            16777216,
                            33554432,
                            67108864,
                            134217728,
                            268435456,
                            536870912,
                            1073741824};
    return s.count(n);
}

bool isPowerOfTwo2(int n)
{
    if (n < 0)
        return false;
    long x = 1;
    while (x <= pow(2,31) - 1) 
    {
        if (x == n)
            return true;
        x =x<<1;
        
        
    }
    return false;
}

int main()
{
    // cout << pow(2,31) - 1;
    cout << isPowerOfTwo2(1024);
}