#include<vector>

using namespace std;

int maxProfit(vector<int> &prices, int fee)
{
    int res = 0;
    int buy = prices[0] + fee;

    for (int i = 1; i < prices.size(); i++)
    {
        buy = min(buy, prices[i] + fee);

        if(prices[i]>buy)
        {
            res += prices[i] - buy;
            buy = prices[i];
        }
    }

    return res;
}