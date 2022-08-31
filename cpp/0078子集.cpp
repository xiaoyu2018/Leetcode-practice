#include<vector>

using namespace std;
vector<vector<int>> res;
vector<int> temp;


void BackTracking(int start,vector<int> &nums)
{
    for (int i = start; i < nums.size(); ++i)
    {
        temp.push_back(nums[i]);
        res.push_back(temp);
        BackTracking(i + 1, nums);
        temp.pop_back();
    }
}

vector<vector<int>> subsets(vector<int> &nums)
{
    res.push_back(temp);
    BackTracking(0, nums);
    return res;
}