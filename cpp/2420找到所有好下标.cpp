#include<vector>

using namespace std;

vector<int> goodIndices(vector<int> &nums, int k)
{
    vector<int> res;
    const int len = nums.size();
    int left_dp[len];
    int right_dp[len];

    for (int i = 0; i < len; i++)
        left_dp[i] = right_dp[i] = 1;

    for (int i = 1; i < len; i++)
    {
        if(nums[i]<=nums[i-1])
            left_dp[i] += left_dp[i - 1];
    }
    for (int i = 1; i < len; i++)
    {
        if(nums[i]>=nums[i-1])
            right_dp[i] += right_dp[i - 1];
    }

    for (int i = k; i < len-k; i++)
    {
        if (left_dp[i - 1] >= k && right_dp[i + k] >= k)
            res.push_back(i);
    }

    return res;
}