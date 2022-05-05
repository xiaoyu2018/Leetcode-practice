#include<vector>
#include<iostream>
#include<math.h>

using namespace std;

int maxSubArray(vector<int> &nums)
{
    if(!nums.size())
        return nums[0];

    int temp = nums[0];
    int res = nums[0];

    for (int i = 1;i<nums.size();++i)
    {
        temp = max(temp + nums[i], nums[i]);
        res = max(res, temp);
    }

    return res;
}

int main()
{
    cout << max(-1, 11);
}