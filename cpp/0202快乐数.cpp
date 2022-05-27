#include<unordered_set>

using namespace std;


bool isHappy(int n)
{
    unordered_set<int> memo;
    int s;
    while (true)
    {
        if(n==1)
            return true;
        if(memo.find(n)!=memo.end())
            return false;

        memo.insert(n);
        s = 0;
        while (n > 0)
        {
            s += (n % 10) * (n % 10);
            n /= 10;
        }
        n = s;


    }
}