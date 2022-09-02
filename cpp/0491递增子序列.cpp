#include<vector>
using namespace std;

vector<vector<int>> res;
vector<int> path;
void BackTracking(const vector<int> &nums, int startIndex)
{
    if (path.size() > 1)
    {
        res.push_back(path);
    }
    int used[201] = {0}; 
    for (int i = startIndex; i < nums.size(); i++)
    {
        if ((!path.empty() && nums[i] < path.back()) || used[nums[i] + 100] == 1)
        {
            continue;
        }
        used[nums[i] + 100] = 1; 
        path.push_back(nums[i]);
        BackTracking(nums, i + 1);
        path.pop_back();
    }
}

vector<vector<int>> findSubsequences(vector<int> &nums)
{
    
    BackTracking(nums, 0);

    return res;
}