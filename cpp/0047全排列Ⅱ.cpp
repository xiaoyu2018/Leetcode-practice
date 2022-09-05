#include<vector>
#include<iostream>
using namespace std;

int d_used[8] = {0};
vector<int> temp;
vector<vector<int>> res;

void BackTracking(vector<int> &nums)
{
    int b_used[21] = {0};

    if(temp.size()==nums.size())
    {
        res.push_back(temp);
        return;
    }

    for (int i=0;i<nums.size();++i)
    {
        if (b_used[nums[i] + 10] || d_used[i])
            continue;

        b_used[nums[i] + 10] = 1;
        d_used[i] = 1;
        temp.push_back(nums[i]);
        BackTracking(nums);
        temp.pop_back();
        d_used[i] = 0;
    }
}

vector<vector<int>> permuteUnique(vector<int> &nums)
{
    BackTracking(nums);
    return res;
}

int main()
{
    vector<int> nums = {1, 1, 2};
    permuteUnique(nums);

    for(vector<int> vec:res)
    {
        for(int v:vec)
        {
            cout << v << " ";
        }
        cout << endl;
    }
}