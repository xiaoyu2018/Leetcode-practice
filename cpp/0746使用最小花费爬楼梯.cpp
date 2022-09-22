#include<vector>

using namespace std;

int minCostClimbingStairs(vector<int> &cost)
{
    int pp = cost[0];
    int p = cost[1];

    for (int i = 2;i<cost.size();i++)
    {
        int temp = cost[i] + min(pp, p);

        pp = p;
        p = temp;
    }

    return min(pp, p);
}