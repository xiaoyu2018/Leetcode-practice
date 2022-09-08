#include<vector>

using namespace std;


//贪心
int maxProfit(vector<int> &prices)
{
    //只要在两天之内有利润就进行一次买入卖出操作
    //无利润则不买

    int res = 0;

    for (int i = 1;i<prices.size();++i)
    {
        int intrests = prices[i] - prices[i - 1];
        res = intrests > 0 ? res + intrests : res;
    }

    return res;
}