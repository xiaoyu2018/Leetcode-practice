#include<vector>
#include<unordered_set>
#include<algorithm>

using namespace std;

vector<vector<int>> res;
vector<int> temp;
    
void backTracking(int start, vector<int> &candidates, int target, int sum)
{
    unordered_set<int> set;
    if (sum == target)
    {
        res.push_back(temp);
        return;
    }

    for (int i = start; i < candidates.size() && sum <= target; ++i)
    {
        int val = candidates[i];
        if (set.find(val)!=set.end())
            continue;
        temp.push_back(val);
        set.insert(val);
        backTracking(i + 1, candidates, target, sum + val);
        temp.pop_back();
    }
}

vector<vector<int>> combinationSum2(vector<int> &candidates, int target)
{
    sort(candidates.begin(),candidates.end());
    backTracking(0, candidates, target, 0);
    return res;
}