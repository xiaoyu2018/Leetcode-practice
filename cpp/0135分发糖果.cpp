#include<vector>
using namespace std;

int candy(vector<int> &ratings)
{
    const int len = ratings.size();
    int allocations[len];

    for (int i = 0; i < len; i++)
    {
        allocations[i] = 1;
    }

    for (int i = 1; i < len; i++)
    {
        if(ratings[i]>ratings[i-1])
            allocations[i] = allocations[i - 1] + 1;
    }

    for (int i = len - 2; i >= 0;i--)
    {
        if(ratings[i]>ratings[i+1])
            allocations[i] = max(allocations[i], allocations[i + 1] + 1);
    }

    int sum = 0;
    for (int i : allocations)
    {
        sum += i;
    }

    return sum;
}