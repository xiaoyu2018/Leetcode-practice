#include<vector>
#include<algorithm>

using namespace std;
vector<int> temp;
vector<vector<int>> res;

void BackTracking(const vector<int> &nums)
{
    if(temp.size()==nums.size())
    {
        res.push_back(temp);
        return;
    }

    for(int i :nums)
    {
        if(find(temp.begin(),temp.end(),i)!=temp.end())
            continue;
        temp.push_back(i);
        BackTracking(nums);
        temp.pop_back();
    }
}

vector<vector<int>> permute(vector<int> &nums)
{
    BackTracking(nums);
    return res;
}