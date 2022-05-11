#include<vector>
#include<iostream>

using namespace std;

// 暴力
int maxProfit1(vector<int> prices)
{
    int profits = 0;
    int size = prices.size();
    for (int i = 0; i<size-1; ++i)
    {
        for (int j = i + 1;j<size;++j)
        {
            if(prices[i]<prices[j])
                profits = max(profits, prices[j] - prices[i]);
        }
    }

    return profits;
}

// 动态规划
// 第i天卖出时，应在前i天的最低点买入
//前i天的最低点与前i-1天有关
int maxProfit2(vector<int> prices)
{
    int min_val = prices[0], res = 0;
    for(int e:prices)
    {
        min_val = min(min_val, e);
        res = max(res, e - min_val);
    }

    return res;
}

int main()
{
    cout << max(1, 2);
}