#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

int majorityElement1(vector<int> &nums)
{
    sort(nums.begin(), nums.end());

    return nums[nums.size() >> 1];
}


int getMajority(vector<int> &nums,int left,int right)
{
    if(left==right)
        return nums[left];
    int mid = (left + right) >> 1;
    int lm = getMajority(nums, left, mid);
    int rm = getMajority(nums, mid+1, right);
    
    if(lm==rm)
        return lm;
    int lm_count = 0;
    int rm_count = 0;
    for (int i = left;i<=right;++i)
    {
        lm_count += !(lm ^ nums[i]);
        rm_count += !(rm ^ nums[i]);
    }

    return lm_count > rm_count ? lm : rm;
}
int majorityElement2(vector<int> &nums)
{
    return getMajority(nums, 0, nums.size() - 1);
}
