#include<vector>
#include<algorithm>
#include <unordered_set>
using namespace std;

vector<vector<int>> res;
vector<int> temp;

void BackTracking(const vector<int>&nums,int start)
{
    unordered_set<int> memo;

    for (int i = start;i<nums.size();++i)
    {
        int val = nums[i];
        if (memo.find(val) == memo.end())
        {
            memo.insert(val);
            temp.push_back(val);
            res.push_back(temp);
            BackTracking(nums, i + 1);
            temp.pop_back();
        }
    }
}

vector<vector<int>> subsetsWithDup(vector<int> &nums)
{
    res.push_back(temp);
    sort(nums.begin(), nums.end());

    BackTracking(nums, 0);
    return res;
}
