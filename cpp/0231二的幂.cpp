#include<iostream>
#include<unordered_set>
#include<math.h>
using namespace std;

bool isPowerOfTwo1(int n)
{
    switch (n)
    {
    case 1:
    case 2:
    case 4:
    case 8:
    case 16:
    case 32:
    case 64:
    case 128:
    case 256:
    case 512:
    case 1024:
    case 2048:
    case 4096:
    case 8192:
    case 16384:
    case 32768:
    case 65536:
    case 131072:
    case 262144:
    case 524288:
    case 1048576:
    case 2097152:
    case 4194304:
    case 8388608:
    case 16777216:
    case 33554432:
    case 67108864:
    case 134217728:
    case 268435456:
    case 536870912:
    case 1073741824:
        return true;
    }
    return false;
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