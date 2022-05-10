#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

int singleNumber1(vector<int> &nums)
{
    int res = 0;
    for(int i :nums)
        res ^= i;
    return res;
}

int singleNumber2(vector<int> &nums)
{
    sort(nums.begin(),nums.end());
    int i = 0;
    for (; i < nums.size() - 1; ++i)
    {
        if(nums[i]!=nums[i+1])
            return nums[i];
        ++i;
    }
    return nums[i];
}

