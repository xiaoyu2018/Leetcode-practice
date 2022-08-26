#include<vector>

using namespace std;

vector<vector<int>> res;
vector<int> temp;

void backTracking(int start,vector<int>&candidates,int target,int sum)
{
    if(sum == target)
    {
        res.push_back(temp);
        return;
    }

    for (int i = start;i<candidates.size()&&sum<=target;++i)
    {
        temp.push_back(candidates[i]);
        backTracking(i, candidates, target, sum + candidates[i]);
        temp.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int> &candidates, int target)
{
    backTracking(0, candidates, target, 0);
    return res;
}