#include<vector>
using namespace std;

bool canPartition(vector<int> &nums)
{
    int sum = 0;
    
    for (int i = 0; i < nums.size(); i++)
    {
        sum += nums[i];
    }
    
    if (sum % 2 == 1)
        return false;
    const int target = sum / 2;
    vector<int> dp(target+1, 0);

    // 开始 01背包
    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = target; j >= nums[i]; j--)
        { 
            dp[j] = max(dp[j], dp[j - nums[i]] + nums[i]);
        }
    }

    return dp[target] == target;
}